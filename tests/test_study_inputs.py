import json
import unittest
from pathlib import Path


class StudyInputTests(unittest.TestCase):
    def test_domain_references_and_units(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'fixtures/study-input.json').read_text())
        from tariffs.catalog import Catalog
        catalog=Catalog(data['document'])
        self.assertGreater(len(catalog.households.by_id),100)
        for h in data['document']['households']:
            self.assertLessEqual(h['income_low'],h['income_high'])
            self.assertGreater(h['weight'],0)
