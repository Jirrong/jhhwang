#!/usr/bin/env ruby
# Render media/disclosure fixtures in memory; never add example work to public data.
require 'jekyll'
require 'tmpdir'
require 'fileutils'
require_relative 'content_media'

root = File.expand_path('..', __dir__)
preview = File.expand_path(ENV['MEDIA_PREVIEW_DIR']) if ENV['MEDIA_PREVIEW_DIR']
raise 'preview must be outside the repository' if preview && (preview == root || preview.start_with?(root + '/'))
Dir.mktmpdir('academic-media-') do |temp|
  # Validate the author's upload format as well as its rendered output.
  FileUtils.mkdir_p(File.join(temp, 'images/news'))
  File.write(File.join(temp, 'images/news/test.svg'), '<svg xmlns="http://www.w3.org/2000/svg"/>')
  valid = {'images' => [{'file' => '/images/news/test.svg', 'alt' => 'A test diagram', 'caption' => 'Test caption', 'kind' => 'graphical'}], 'abstract' => 'Text.'}
  check = ->(entry) { ContentMedia.check(entry, temp, 'Fixture', legacy_folder: 'images/news') }
  raise 'valid image metadata was rejected' unless check.call(valid).empty?
  raise 'legacy filenames must still work' unless check.call({'image' => 'test.svg'}).empty?
  raise 'optional fields must be optional' unless check.call({}).empty?
  [
    valid.merge('abstract' => ['not text']),
    {'images' => 'not a list'},
    {'images' => [nil]},
    {'images' => [{'file' => '/images/news/test.svg', 'alt' => ''}]},
    {'images' => [{'file' => '/images/news/missing.png', 'alt' => 'Missing'}]},
    {'images' => [{'file' => '/images/../../_config.yml', 'alt' => 'Traversal'}]},
    {'images' => [{'file' => 'https://example.org/photo.png', 'alt' => 'Remote'}]},
    {'images' => [{'file' => '/images/news/test.svg', 'alt' => 'Text', 'kind' => 'invalid'}]}
  ].each { |entry| raise "invalid metadata was accepted: #{entry}" if check.call(entry).empty? }

  site = Jekyll::Site.new(Jekyll.configuration('source' => root, 'destination' => preview || File.join(temp, '_site'), 'safe' => true, 'quiet' => true))
  site.read
  graph = {'file' => '/images/layout-test/graph.svg', 'alt' => 'TEST_ONLY complete landscape diagram', 'caption' => 'TEST_ONLY landscape <caption>', 'kind' => 'graphical'}
  photo = {'file' => '/images/layout-test/portrait.svg', 'alt' => 'TEST_ONLY portrait image', 'kind' => 'photo'}
  abstract = "TEST_ONLY A long abstract describing the layout fixture. This text must stay collapsed until requested. #{'A longer sentence tests wrapping and comfortable reading width. ' * 12}\n\nA second paragraph with **emphasis** and an inline equation $\\Delta G = \\Delta H - T\\Delta S$."
  site.data['publist'] = [
    {'title' => 'TEST_ONLY Selected paper with graphical abstract', 'authors' => 'Test Author, Jiho Hwang, and Another Author', 'image' => 'dummy.png', 'image_alt' => 'TEST_ONLY legacy figure', 'description' => 'A **test** summary.', 'abstract' => abstract, 'link' => {'url' => 'https://example.org/paper', 'display' => 'Test Journal (2026)'}, 'highlight' => 1},
    {'title' => 'TEST_ONLY Selected paper without optional fields', 'authors' => 'Test Author', 'highlight' => 1},
    {'title' => 'TEST_ONLY Paper with two images', 'authors' => 'Test Author', 'highlight' => 0, 'images' => [graph, photo]},
    {'title' => 'TEST_ONLY Hidden draft paper', 'authors' => '', 'highlight' => 1, 'published' => false}
  ]
  site.data['conferences'] = [
    {'id' => 'test-conference', 'meeting' => 'TEST_ONLY Meeting', 'date' => '2026', 'location' => 'Test City', 'type' => 'Poster presentation', 'title' => 'TEST_ONLY Poster with photos and a full text abstract', 'authors' => 'Jiho Hwang and Test Author', 'session' => 'Test session', 'abstract_number' => '123', 'abstract' => abstract, 'images' => [graph, photo]},
    {'id' => 'bare-conference', 'meeting' => 'TEST_ONLY Meeting', 'date' => '2025', 'type' => 'Talk', 'title' => 'TEST_ONLY Bare conference', 'authors' => 'Test Author'},
    {'id' => 'hidden-conference', 'title' => 'TEST_ONLY Hidden draft conference', 'published' => false}
  ]
  site.data['news'] = [
    {'id' => 'test-news', 'date' => 'November 2026', 'title' => 'TEST_ONLY News with two photographs', 'headline' => 'TEST_ONLY Full news text with **Markdown**.', 'summary' => 'TEST_ONLY Brief news.', 'images' => [photo, graph]},
    {'date' => 'October 2026', 'headline' => 'TEST_ONLY Bare news.'},
    {'date' => '2026', 'headline' => 'TEST_ONLY Hidden draft news', 'published' => false}
  ]
  site.generate
  site.render
  publications = site.pages.find { |page| page.url == '/publications/' }.output
  news = site.pages.find { |page| page.url == '/news/' }.output
  home = site.pages.find { |page| page.url == '/' }.output
  raise 'papers must appear once each, including selected ones' unless publications.scan(/<article class="well record-card publication-card/).size == 3 && publications.scan(/<h3[^>]*>.*?TEST_ONLY Selected paper with graphical abstract.*?<\/h3>/m).size == 1
  raise 'selected papers must retain their badge' unless publications.scan('publication-selected').size == 2
  raise 'old two-column grid was rendered' if publications.include?('col-sm-6')
  raise 'conference cards are missing' unless publications.scan('class="well record-card conference-card"').size == 2
  raise 'both supplied abstracts should render as initially closed disclosures' unless publications.scan('<details class="abstract-disclosure">').size == 2 && !publications.match?(/<details[^>]*\sopen(?:\s|=|>)/)
  raise 'abstract Markdown did not render' unless publications.include?('<strong>emphasis</strong>')
  raise 'author name emphasis is missing' unless publications.include?('<strong>Jiho Hwang</strong>')
  raise 'legacy image compatibility was lost' unless publications.include?('/jhhwang/images/pubpic/dummy.png')
  raise 'canonical gallery or escaped caption is missing' unless publications.include?('entry-media-multiple') && publications.include?('TEST_ONLY landscape &lt;caption&gt;')
  raise 'images need a complete-original link and accessible text' unless publications.include?('target="_blank" rel="noopener" aria-label="Open full-size image: TEST_ONLY complete landscape diagram"')
  raise 'missing fields created empty media or links' if (publications + news).match?(/(?:href|src)=""/)
  raise 'news cards or gallery are missing' unless news.scan('class="well record-card news-card"').size == 2 && news.include?('/jhhwang/images/layout-test/portrait.svg')
  raise 'news without an explicit ID needs an anchor' unless news.include?('id="news-2"')
  raise 'home brief must link to the complete news and omit its photos' unless home.include?('href="/jhhwang/news/#test-news"') && home.include?('TEST_ONLY Brief news.') && !home.include?('/images/layout-test/')
  raise 'draft content leaked into public pages' if (publications + news + home).include?('TEST_ONLY Hidden draft')

  # Optional isolated preview, outside the source tree, for real browser checks.
  if preview
    site.write
    FileUtils.mkdir_p(File.join(preview, 'images/layout-test'))
    [[1200, 360, 'graph'], [450, 640, 'portrait']].each do |width, height, name|
      File.write(File.join(preview, "images/layout-test/#{name}.svg"), "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"#{width}\" height=\"#{height}\" viewBox=\"0 0 #{width} #{height}\"><rect x=\"2\" y=\"2\" width=\"#{width - 4}\" height=\"#{height - 4}\" fill=\"#eff4f7\" stroke=\"#57778c\" stroke-width=\"4\"/><path d=\"M20 #{height - 20} L#{width / 2} 30 L#{width - 20} #{height - 20}\" fill=\"none\" stroke=\"#57778c\" stroke-width=\"4\"/><text x=\"30\" y=\"#{height / 2}\" font-size=\"24\" fill=\"#294b60\">TEST_ONLY #{name} layout fixture</text></svg>")
    end
  end
end
puts 'PASS: full-width single-list papers, conferences, news galleries, legacy images, closed abstracts, optional fields, draft filtering, and upload validation; public data was not modified.'
