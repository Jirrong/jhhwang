#!/usr/bin/env ruby
# Render an imported social-post fixture outside the public source tree.
require 'jekyll'
require 'tmpdir'
require 'fileutils'
require 'json'
require 'open3'
require 'cgi'

root = File.expand_path('..', __dir__)
Dir.mktmpdir('linkedin-render-') do |temp|
  %w[_config.yml _includes _layouts _data].each { |name| FileUtils.cp_r(File.join(root, name), temp) }
  FileUtils.mkdir_p(File.join(temp, '_pages'))
  %w[home.md blog.md].each { |name| FileUtils.cp(File.join(root, '_pages', name), File.join(temp, '_pages', name)) }
  FileUtils.cp(File.join(root, 'search.json'), temp)
  text = "TEST_ONLY <img src=x onerror=\"literal\">\n\n# Keep this as text, **not Markdown**.\n{{ site.email }} {% include private %}\nEmoji 🧪 and 한국어."
  record = {'id' => 'urn:li:share:1234567890', 'author' => 'urn:li:person:TEST_AUTHOR', 'visibility' => 'PUBLIC', 'lifecycleState' => 'PUBLISHED', 'publishedAt' => 1774692000000, 'commentary' => text}
  fixture = File.join(temp, 'posts.json')
  File.write(fixture, JSON.generate('elements' => [record]))
  output, status = Open3.capture2e({'LINKEDIN_ACCESS_TOKEN' => nil}, 'python3', File.join(root, 'scripts/sync_linkedin.py'), '--root', temp, '--input', fixture, '--author', record['author'])
  raise "fixture import failed: #{output}" unless status.success?
  site = Jekyll::Site.new(Jekyll.configuration('source' => temp, 'destination' => File.join(temp, '_site'), 'safe' => true, 'quiet' => true))
  site.read
  site.generate
  site.render
  raise 'fixture post was not read' unless site.posts.docs.size == 1
  post = site.posts.docs.first
  match = post.output.match(/<div class="linkedin-text"[^>]*>(.*?)<\/div>/m)
  raise 'visible post text changed during Jekyll rendering' unless match && CGI.unescapeHTML(match[1]) == text
  raise 'imported literal HTML executed as markup' if post.output.include?('<img src=x onerror=')
  raise 'imported text created a Markdown heading' if post.output.include?('<h1 id="keep')
  raise 'imported post reserves a TOC' if post.output.include?('notebook-toc')
  %w[/ /blog/].each do |url|
    html = site.pages.find { |page| page.url == url }.output
    raise "literal social-post title became markup on #{url}" if html.include?('<img src=x onerror=')
  end
  search = JSON.parse(site.pages.find { |page| page.url == '/search.json' }.output)
  raise 'imported post is missing from search' unless search.size == 1 && search[0]['content'].include?('TEST_ONLY')
  feed = site.pages.find { |page| page.url == '/feed.xml' }
  raise 'imported post is missing from RSS' unless feed && feed.output.include?('urn:li:share:1234567890')
end
puts 'PASS: imported original text, literal HTML/Liquid, blog/home listings, search, RSS, and no empty TOC; no fixture was published.'
