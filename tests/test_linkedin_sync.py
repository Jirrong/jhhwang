from datetime import datetime, timezone
from html import unescape
import importlib.util
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('sync_linkedin', Path(__file__).resolve().parents[1] / 'scripts/sync_linkedin.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)
AUTHOR = 'urn:li:person:TEST_AUTHOR'


def post(**updates):
    item = {
        'id': 'urn:li:share:1234567890', 'author': AUTHOR,
        'visibility': 'PUBLIC', 'lifecycleState': 'PUBLISHED',
        'publishedAt': int(datetime(2026, 3, 28, 10, 0, tzinfo=timezone.utc).timestamp() * 1000),
        'commentary': 'Original title\n\nUnchanged text, #Chemistry, $5, **literal Markdown**, and an emoji 🧪.',
    }
    item.update(updates)
    return item


class ImportTests(unittest.TestCase):
    def test_preserves_visible_text_original_date_and_literal_template_syntax(self):
        text = '\nOriginal title\n\n# No Markdown heading\n<script>literal</script> {{ site.email }} {% include private %}\nEnglish and 한국어 🧪'
        with tempfile.TemporaryDirectory() as root:
            result = sync.mirror_posts(root, [post(commentary=text)], AUTHOR)
            path = Path(root, '_posts', result['changed'][0])
            content = path.read_text()
            body = re.search(r'<div class="linkedin-text" markdown="0">(.*?)</div>', content, re.S)[1]
            self.assertEqual(unescape(body), text)
            self.assertNotIn('{{ site.email }}', body)
            self.assertNotIn('{% include private %}', body)
            self.assertIn('date: "2026-03-28 19:00:00 +0900"', content)
            self.assertIn('math: false', content)
            self.assertIn('toc: false', content)
            self.assertIn('https://www.linkedin.com/feed/update/urn:li:share:1234567890/', content)

    def test_repeated_sync_is_unchanged_and_source_edits_update_one_stable_file(self):
        with tempfile.TemporaryDirectory() as root:
            first = sync.mirror_posts(root, [post()], AUTHOR)
            again = sync.mirror_posts(root, [post()], AUTHOR)
            updated = sync.mirror_posts(root, [post(commentary='Edited original text')], AUTHOR)
            self.assertEqual(again['changed'], [])
            self.assertEqual(again['unchanged'], first['changed'])
            self.assertEqual(updated['changed'], first['changed'])
            self.assertEqual(len(list(Path(root, '_posts').glob('*.md'))), 1)
            self.assertIn('Edited original text', Path(root, '_posts', first['changed'][0]).read_text())

    def test_does_not_import_other_authors_private_posts_drafts_or_reshares(self):
        records = [post(author='urn:li:person:OTHER'), post(visibility='CONNECTIONS'), post(lifecycleState='DRAFT'), post(reshareContext={'parent': 'urn:li:share:987'})]
        with tempfile.TemporaryDirectory() as root:
            result = sync.mirror_posts(root, records, AUTHOR)
            self.assertEqual(result['skipped'], 4)
            self.assertFalse(list(Path(root, '_posts').glob('*.md')))

    def test_downloads_multiple_images_once_and_recovers_a_missing_asset(self):
        class Images:
            calls = 0
            def image(self, urn):
                self.calls += 1
                return b'TEST_ONLY original image bytes', 'png'
        client = Images()
        item = post(content={'multiImage': {'images': [{'id': 'urn:li:image:ONE', 'altText': 'First image'}, {'id': 'urn:li:image:TWO', 'altText': 'Second image'}]}})
        with tempfile.TemporaryDirectory() as root:
            result = sync.mirror_posts(root, [item], AUTHOR, client)
            self.assertEqual(client.calls, 2)
            content = Path(root, '_posts', result['changed'][0]).read_text()
            self.assertIn('alt="First image"', content)
            self.assertIn('alt="Second image"', content)
            self.assertEqual(len(list(Path(root, 'assets/linkedin').glob('*.png'))), 2)
            sync.mirror_posts(root, [item], AUTHOR, client)
            self.assertEqual(client.calls, 2)
            next(Path(root, 'assets/linkedin').glob('*.png')).unlink()
            recovered = sync.mirror_posts(root, [item], AUTHOR, client)
            self.assertTrue(recovered['changed'])
            self.assertEqual(len(list(Path(root, 'assets/linkedin').glob('*.png'))), 2)

    def test_hashtag_and_mention_tokens_keep_their_visible_words(self):
        self.assertEqual(sync.visible_text('Hello @[Jiho Hwang](urn:li:person:abc), {hashtag|\\#|Chemistry}!'), 'Hello Jiho Hwang, #Chemistry!')

    def test_invalid_ids_and_unexpected_image_hosts_are_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(ValueError):
                sync.mirror_posts(root, [post(id='../../outside')], AUTHOR)
        with patch.object(sync, 'urlopen') as fetch:
            for url in ['http://media.licdn.com/image.png', 'https://example.com/image.png', 'https://media.licdn.com.example.org/image.png']:
                with self.assertRaises(ValueError): sync.download_image(url)
            fetch.assert_not_called()


if __name__ == '__main__':
    unittest.main()
