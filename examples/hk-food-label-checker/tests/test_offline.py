# confidentiality: public-approved
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core import IngredientExtractor
from knowledge import KnowledgeBase
from make_demo_data import make_demo
from script_checker import TraditionalChineseChecker


class OfflineChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.path = Path(cls.tmp.name) / 'demo.xlsx'
        make_demo(cls.path)
        cls.kb = KnowledgeBase(str(cls.path))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_exact_and_alias_have_same_identity(self):
        a = self.kb.get_info('演示成分甲')
        b = self.kb.get_info('测试别名A')
        self.assertEqual(a.additive_id, b.additive_id)
        self.assertEqual((a.match_type, b.match_type), ('exact', 'alias'))

    def test_common_and_unknown_do_not_become_additives(self):
        self.assertTrue(self.kb.get_info('水').is_common_food)
        self.assertFalse(self.kb.get_info('完全未知的测试词xyz').found)

    def test_numeric_ingredient_names_are_preserved(self):
        extractor = IngredientExtractor(api_key='')
        result = extractor._parse_ingredient_response('{"ingredients":["5′-核苷酸","5′-核苷酸"]}')
        self.assertEqual(result.ingredients, ['5′-核苷酸'])

    def test_malformed_response_fails(self):
        self.assertFalse(IngredientExtractor(api_key='')._parse_ingredient_response('not json').success)

    def test_layout_keeps_original_and_suggestion(self):
        result = IngredientExtractor(api_key='')._parse_layout_response('{"blocks":[{"role":"field","label_original":"信息","label_hk":"資訊","value_original":"测试","value_hk":"測試"}]}')
        self.assertTrue(result.success)
        self.assertEqual(result.blocks[0].label_original, '信息')

    def test_model_setting_read_on_construction(self):
        with patch.dict(os.environ, {'QWEN_VL_MODEL': 'example-model'}):
            self.assertEqual(IngredientExtractor(api_key='').model, 'example-model')

    def test_conversion_marks_change(self):
        result = TraditionalChineseChecker().check_text('测试标签')
        self.assertTrue(result.has_simplified)
        self.assertNotEqual(result.original_text, result.converted_text)

    def test_false_alias_flag_not_used_as_fuzzy_candidate(self):
        self.kb.alias_df.loc[:, 'is_fuzzy_candidate'] = 'False'
        self.kb.alias_map['specialalias'] = (self.kb.master_df.iloc[0], self.kb.alias_df.iloc[0])
        self.assertNotIn('specialalias', self.kb._get_fuzzy_candidates())


if __name__ == '__main__':
    unittest.main()

