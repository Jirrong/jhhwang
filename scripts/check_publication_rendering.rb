#!/usr/bin/env ruby
# Render fixture records in memory; never add example papers to the live data.
require 'jekyll'
root = File.expand_path('..', __dir__)
site = Jekyll::Site.new(Jekyll.configuration('source' => root, 'destination' => File.join(root, '_site'), 'safe' => true, 'quiet' => true))
site.read
site.data['publist'] = [
  {'title' => 'TEST_ONLY Highlight with figure', 'authors' => 'Test Author', 'image' => 'dummy.png', 'description' => 'A **test** summary.', 'link' => {'url' => 'https://example.org/paper', 'display' => 'Test Journal (2026)'}, 'highlight' => 1, 'published' => true},
  {'title' => 'TEST_ONLY Highlight without optional fields', 'authors' => 'Test Author', 'highlight' => 1},
  {'title' => 'TEST_ONLY Full list only', 'authors' => 'Test Author', 'highlight' => 0},
  {'title' => 'TEST_ONLY Hidden draft', 'authors' => '', 'highlight' => 1, 'published' => false}
]
site.generate
site.render
page = site.pages.find { |p| p.url == '/publications/' }
html = page.output
raise 'selected-paper cards are missing or include a draft' unless html.scan('class="well publication-highlight"').size == 2
raise 'full list must contain all three published records' unless html.scan('class="publication-entry"').size == 3
raise 'draft publication was rendered' if html.include?('TEST_ONLY Hidden draft')
raise 'missing optional fields produced an empty link or image' if html.match?(/(?:href|src)=""/)
raise 'selected-paper figure is missing' unless html.include?('/jhhwang/images/pubpic/dummy.png')
raise 'full-list-only item appeared as a selected card' unless html.scan('TEST_ONLY Full list only').size == 1
raise 'selected publication should also be in the full list' unless html.scan('TEST_ONLY Highlight with figure').size == 3 # title, figure alt text, full list
puts 'PASS: original-style publication cards, full list, optional fields, and draft filtering render correctly; live data was not modified.'
