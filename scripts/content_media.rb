require 'uri'

# Shared authoring checks for optional local images and abstract text.
module ContentMedia
  def self.check(record, root, label, legacy_folder: nil)
    errors = []
    if record.key?('abstract') && !record['abstract'].is_a?(String)
      errors << "#{label}: abstract must be text"
    end
    validate_file = lambda do |file, name|
      unless file.is_a?(String) && file.start_with?('/images/', '/assets/') && !file.match?(/[?#]/)
        errors << "#{name}: use a local /images/... or /assets/... image path"
        next
      end
      path = File.expand_path(URI::DEFAULT_PARSER.unescape(file).delete_prefix('/'), root)
      allowed = path.start_with?(File.join(root, 'images') + '/', File.join(root, 'assets') + '/')
      extension = File.extname(path).downcase
      errors << "#{name}: missing image #{file}" unless allowed && File.file?(path)
      errors << "#{name}: expected PNG, JPEG, WebP, GIF, or SVG" unless %w[.png .jpg .jpeg .webp .gif .svg].include?(extension)
    end
    if record.key?('images')
      unless record['images'].is_a?(Array)
        errors << "#{label}: images must be a list of file/alt/caption records"
        return errors
      end
      record['images'].each_with_index do |image, index|
        name = "#{label}: images[#{index}]"
        unless image.is_a?(Hash)
          errors << "#{name}: expected a file/alt/caption record"
          next
        end
        validate_file.call(image['file'], name)
        errors << "#{name}: add descriptive alt text" unless image['alt'].is_a?(String) && !image['alt'].strip.empty?
        errors << "#{name}: caption must be text" if image.key?('caption') && !image['caption'].is_a?(String)
        if image.key?('kind') && !['', 'photo', 'graphical'].include?(image['kind'])
          errors << "#{name}: kind must be photo or graphical"
        end
      end
    end
    if record['image'] && record['image'] != ''
      file = record['image']
      if !file.is_a?(String)
        errors << "#{label}: image must be a filename or local image path"
      else
        file = '/' + legacy_folder.to_s.sub(%r{\A/}, '').sub(%r{/?\z}, '/') + file unless file.start_with?('/')
        validate_file.call(file, "#{label}: image")
      end
    end
    %w[image_alt image_caption].each do |field|
      errors << "#{label}: #{field} must be text" if record.key?(field) && !record[field].is_a?(String)
    end
    errors
  end
end
