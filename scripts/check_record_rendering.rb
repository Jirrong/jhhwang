#!/usr/bin/env ruby
# Build fixture collections in a temporary site; leave public records untouched.
require 'jekyll'
require 'tmpdir'
require 'fileutils'
require 'open3'
require 'rbconfig'

root = File.expand_path('..', __dir__)
Dir.mktmpdir('academic-records-') do |temp|
  %w[_config.yml _layouts _includes _data].each { |name| FileUtils.cp_r(File.join(root, name), temp) }
  %w[_pages _research _resources assets/resources].each { |name| FileUtils.mkdir_p(File.join(temp, name)) }
  %w[research.md resources.md].each { |name| FileUtils.cp(File.join(root, '_pages', name), File.join(temp, '_pages', name)) }
  %w[slides.pdf talk.pptx].each { |name| File.write(File.join(temp, 'assets/resources', name), 'TEST_ONLY file') }
  write_record = lambda do |collection, name, data|
    File.write(File.join(temp, "_#{collection}", "#{name}.md"), data.to_yaml + "---\n\n## Notes\n\nTEST_ONLY body.\n")
  end
  write_record.call('research', 'older-project', {'title' => 'TEST_ONLY Older project', 'summary' => 'Older summary', 'period' => '2024', 'order' => 7})
  write_record.call('research', 'newer-project', {'title' => 'TEST_ONLY New & <b>project</b>', 'summary' => '<script>test</script>', 'period' => '2025–present', 'order' => 8, 'topics' => ['A & B']})
  write_record.call('research', 'hidden-project', {'title' => 'TEST_ONLY HIDDEN PROJECT', 'order' => 99, 'published' => false})
  write_record.call('resources', 'older-seminar', {'title' => 'TEST_ONLY Older seminar', 'summary' => 'Earlier material', 'order' => 1, 'files' => [{'label' => 'Slides', 'url' => '/assets/resources/slides.pdf'}]})
  write_record.call('resources', 'newer-seminar', {
    'title' => 'TEST_ONLY Newer seminar', 'summary' => 'Seminar summary', 'order' => 2, 'kind' => 'Seminar', 'event' => 'Reading group', 'event_date' => 'November 2026',
    'files' => [{'label' => 'Slides (PDF)', 'url' => '/assets/resources/slides.pdf'}, {'label' => 'Presentation (PPTX)', 'url' => '/assets/resources/talk.pptx'}, {'label' => 'Reference', 'url' => 'https://example.org/reference'}]
  })
  write_record.call('resources', 'hidden-seminar', {'title' => 'TEST_ONLY HIDDEN RESOURCE', 'published' => false, 'files' => [{'url' => '/assets/resources/not-uploaded.pdf'}]})
  site = Jekyll::Site.new(Jekyll.configuration('source' => temp, 'destination' => File.join(temp, '_site'), 'safe' => true, 'quiet' => true))
  site.read
  site.generate
  site.render
  projects = site.pages.find { |page| page.url == '/research/' }.output
  materials = site.pages.find { |page| page.url == '/resources/' }.output
  raise 'research boxes must stack one per project' unless projects.scan('class="well record-card research-card"').size == 2
  raise 'research order must put larger order first' unless projects.index('TEST_ONLY New &amp; &lt;b&gt;project&lt;/b&gt;') < projects.index('TEST_ONLY Older project')
  raise 'summary must be escaped' unless projects.include?('&lt;script&gt;test&lt;/script&gt;')
  raise 'resources order is wrong' unless materials.index('TEST_ONLY Newer seminar') < materials.index('TEST_ONLY Older seminar')
  raise 'resource cards or multi-file buttons missing' unless materials.scan('class="well record-card resource-card"').size == 2 && materials.scan('class="btn btn-default"').size == 4
  raise 'local materials must use the site base path and download' unless materials.include?('href="/jhhwang/assets/resources/slides.pdf" download') && materials.include?('href="/jhhwang/assets/resources/talk.pptx" download')
  raise 'external links must retain their URL' unless materials.include?('href="https://example.org/reference">Reference</a>')
  raise 'optional event metadata is missing' unless materials.include?('November 2026 · Reading group')
  raise 'missing optional metadata created an empty href' if (projects + materials).include?('href=""')
  %w[research resources].each do |label|
    docs = site.collections.fetch(label).docs
    raise 'drafts leaked into collection documents' unless docs.size == 2 && docs.none? { |doc| doc.basename_without_ext.start_with?('hidden') }
    raise 'record detail pages are missing' unless docs.all? { |doc| doc.write? && doc.output.include?('TEST_ONLY body.') && doc.output.include?('class="notebook-content"') }
  end
  raise 'drafts leaked into indexes' if (projects + materials).include?('HIDDEN')
  validator = File.join(root, 'scripts/check_records.rb')
  output, status = Open3.capture2e(RbConfig.ruby, validator, temp)
  raise "valid records failed file validation: #{output}" unless status.success?
  File.delete(File.join(temp, 'assets/resources/talk.pptx'))
  output, status = Open3.capture2e(RbConfig.ruby, validator, temp)
  raise 'a missing seminar upload was accepted' if status.success? || !output.include?('missing local file /assets/resources/talk.pptx')
end
puts 'PASS: stacked records, sorting, multi-file downloads, detail pages, optional fields, escaping, unpublished records, and upload validation; public data was not modified.'
