#!/usr/bin/env ruby
require 'yaml'
require 'uri'

root = File.expand_path('..', __dir__)
load_yaml = ->(path) { YAML.safe_load(File.read(File.join(root, path)), aliases: false) }
errors = []
cv = load_yaml.call('_data/cv.yml')
identity = cv.fetch('identity', {})
%w[name role institution department email github portrait introduction].each do |field|
  errors << "CV identity: #{field} is required" unless identity[field].is_a?(String) && !identity[field].strip.empty?
end
{
  'education' => %w[dates degree institution],
  'research_experience' => %w[dates title institution],
  'research_interests' => %w[id title description],
  'awards' => %w[date title organization],
  'presentations' => %w[title authors],
  'activities' => %w[dates title institution],
  'skills' => %w[label items]
}.each do |section, fields|
  entries = cv[section]
  unless entries.is_a?(Array)
    errors << "CV #{section}: expected a list"
    next
  end
  entries.each_with_index do |entry, index|
    fields.each do |field|
      errors << "CV #{section}[#{index}]: #{field} is required" unless entry[field].is_a?(String) && !entry[field].strip.empty?
    end
  end
end
portrait = identity.fetch('portrait', '').sub(%r{\A/}, '')
errors << 'CV portrait file does not exist' unless File.file?(File.join(root, portrait))
papers = load_yaml.call('_data/publist.yml')
if !papers.is_a?(Array)
  errors << '_data/publist.yml must be a YAML list (use [] when empty)'
else
  papers.each_with_index do |paper, index|
    unless paper.is_a?(Hash)
      errors << "Publication #{index}: expected a record"
      next
    end
    if paper.key?('published') && ![true, false].include?(paper['published'])
      errors << "Publication #{index}: published must be true or false"
    end
    if paper.key?('highlight') && ![0, 1].include?(paper['highlight'])
      errors << "Publication #{index}: highlight must be 0 or 1"
    end
    next if paper['published'] == false
    %w[title authors].each do |field|
      errors << "Publication #{index}: #{field} is required" unless paper[field].is_a?(String) && !paper[field].strip.empty?
    end
    if paper['link'] && !paper['link'].is_a?(Hash)
      errors << "Publication #{index}: link must contain url/display fields"
      next
    end
    url = paper.fetch('link', {}).fetch('url', '').to_s
    unless url.empty?
      begin
        parsed = URI.parse(url)
        errors << "Publication #{index}: use an HTTP(S) publication URL" unless %w[http https].include?(parsed.scheme) && parsed.host
      rescue URI::InvalidURIError
        errors << "Publication #{index}: invalid URL"
      end
    end
    image = paper.fetch('image', '').to_s
    unless image.empty?
      path = File.expand_path(image, File.join(root, 'images/pubpic'))
      errors << "Publication #{index}: missing image #{image}" unless path.start_with?(File.join(root, 'images/pubpic') + '/') && File.file?(path)
    end
  end
end
abort(errors.join("\n")) unless errors.empty?
puts "PASS: CV records and #{papers.count { |p| p['published'] != false }} public publication records are valid."
