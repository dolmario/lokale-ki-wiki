import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wiki_auswahl as w

class SelectionTest(unittest.TestCase):
    def choice(self, answer='J, J, N, N, J, N', finish='stop'):
        return {'message': {'content': answer}, 'finish_reason': finish}

    def test_incomplete_output_is_not_a_decision(self):
        for answer, finish in [('J, J', 'stop'), ('J, J, N, N, J, N', 'length'), ('J, J, N, N, J, X', 'stop')]:
            with self.assertRaises(ValueError):
                w.decode(self.choice(answer, finish))

    def test_confidence_cannot_silently_attach_to_wrong_field(self):
        choice = self.choice()
        choice['logprobs'] = {'content': [{'token': 'N', 'top_logprobs': [{'token': 'N', 'logprob': -.1}]}]*6}
        with self.assertRaises(ValueError):
            w.decode(choice)

    def test_non_loopback_or_credentials_rejected(self):
        for endpoint in ['https://example.com', 'http://127.0.0.1@evil.example', 'http://localhost/api', 'http://127.0.0.1/?x=1']:
            with self.assertRaises(ValueError):
                w.local_endpoint(endpoint)

    def setup_files(self, root):
        source = root/'quelle.md'
        source.write_text('Eine gepruefte eigene Beispielquelle.', encoding='utf-8')
        record = w.decode(self.choice('N, J, N, N, N, N'))
        record.update(source_name=source.name, source_sha256=w.digest(source.read_bytes()))
        result = root/'auswahl.json'
        result.write_bytes(w.json_bytes(record))
        return source, result

    def test_manual_review_can_overrule_unreliable_model_and_keeps_source_exact(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, result = self.setup_files(root)
            with self.assertRaises(ValueError):
                w.deliver(source, result, root/'projekt', False, 'accept')
            proof = w.deliver(source, result, root/'projekt', True, 'accept')
            self.assertTrue(proof['review_overrode_model'])
            self.assertFalse(proof['native_ingest'])
            self.assertEqual((root/'projekt/raw/sources/quelle.md').read_bytes(), source.read_bytes())
            with self.assertRaises(FileExistsError):
                w.deliver(source, result, root/'projekt', True, 'accept')

    def test_changed_source_does_not_reuse_old_selection(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, result = self.setup_files(root)
            source.write_text('Geaenderte Quelle.', encoding='utf-8')
            with self.assertRaises(ValueError):
                w.deliver(source, result, root/'projekt', True, 'accept')
            self.assertFalse((root/'projekt').exists())

if __name__ == '__main__':
    unittest.main()
