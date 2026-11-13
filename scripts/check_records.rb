#!/usr/bin/env ruby
# Check author-managed project/seminar metadata and local download paths.
require 'yaml'
require 'uri'

root = File.expand_path(ARGV.fetch(0, '..'), ARGV.empty? ? __dir__ : Dir.pwd)
errors = []
counts = {}
present = ->(value) { value.is_a?(String) && !value.strip.empty? }

%w[research resources].each do |collection|
  counts[collection] = 0
  orders = {}
  Dir.glob(File.join(root, "_#{collection}", '*.{md,markdown}')).sort.each do |path|
    name = path.delete_prefix(root + '/')
    begin
      front = File.read(path).match(/\A---\s*\n(.*?)\n---\s*(?:\n|\z)/m)
      raise 'expected YAML front matter between --- lines' unless front
      record = YAML.safe_load(front[1], aliases: false)
      raise 'front matter must be a mapping' unless record.is_a?(Hash)
      if record.key?('published') && ![true, false].include?(record['published'])
        errors << "#{name}: published must be true or false"
      end
      next if record['published'] == false
      counts[collection] += 1
      fields = collection == 'research' ? %w[title summary period] : %w[title summary]
      fields.each { |field| errors << "#{name}: #{field} is required" unless present.call(record[field]) }
      order = record['order']
      if !order.is_a?(Integer)
        errors << "#{name}: order must be an integer (larger numbers appear first)"
      elsif orders.key?(order)
        errors << "#{name}: order #{order} is already used by #{orders[order]}"
      else
        orders[order] = name
      end
      %w[program institution status kind event event_date].each do |field|
        errors << "#{name}: #{field} must be text" if record.key?(field) && !record[field].is_a?(String)
      end
      if record.key?('topics') && !(record['topics'].is_a?(Array) && record['topics'].all? { |topic| present.call(topic) })
        errors << "#{name}: topics must be a list of nonempty labels"
      end
      files = record.fetch('files', [])
      unless files.is_a?(Array)
        errors << "#{name}: files must be a list of label/url records"
        next
      end
      errors << "#{name}: add at least one material before publishing a resource" if collection == 'resources' && files.empty?
      files.each_with_index do |file, index|
        label = "#{name}: files[#{index}]"
        unless file.is_a?(Hash) && present.call(file['label']) && present.call(file['url'])
          errors << "#{label}: label and url are required"
          next
        end
        begin
          uri = URI.parse(file['url'])
          if %w[http https].include?(uri.scheme) && uri.host
            next
          elsif !uri.scheme && !uri.host && uri.path.start_with?('/assets/')
            local = File.expand_path(URI::DEFAULT_PARSER.unescape(uri.path).delete_prefix('/'), root)
            unless local.start_with?(File.join(root, 'assets') + '/') && File.file?(local)
              errors << "#{label}: missing local file #{file['url']}"
            end
          else
            errors << "#{label}: use /assets/... or an HTTP(S) URL"
          end
        rescue URI::InvalidURIError
          errors << "#{label}: invalid URL"
        end
      end
    rescue StandardError => error
      errors << "#{name}: #{error.message}"
    end
  end
end
abort(errors.join("\n")) unless errors.empty?
puts "PASS: #{counts['research']} research projects and #{counts['resources']} resources have valid metadata and file links."
