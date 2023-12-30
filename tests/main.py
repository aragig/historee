import unittest
from historee import HistoryManager
import os
import csv


class TestHistoryManager(unittest.TestCase):

    test_file_path = "test_history.csv"

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_load_history_from_file(self):
        # CSVファイルからのデータ読み込みをテスト
        manager = HistoryManager(self.test_file_path)
        action = "/Users/mopipico/Projects/site_101010.fun/content/posts/analog/di/type-71-hybrid-direct-box/eyecatch.jpg"
        self.assertTrue(manager.history_exists(action))


    def test_add_or_update_history(self):
        # 履歴の追加と更新をテスト
        manager = HistoryManager(self.test_file_path)
        manager.add_history("アクションテスト１")
        self.assertTrue(manager.history_exists("アクションテスト１"))


    def test_add_or_update_history2(self):
        # 履歴の追加と更新をテスト
        manager = HistoryManager(self.test_file_path)
        manager.add_history("アクションテスト２")
        self.assertTrue(manager.history_exists("アクションテスト２"))

    def test_is_newer_than_history(self):
        # 履歴の更新日時を比較するテスト
        manager = HistoryManager(self.test_file_path)
        manager.add_history("アクションテスト３")
        self.assertFalse(manager.is_newer_than_history("アクションテスト３", 0))
        self.assertTrue(manager.is_newer_than_history("アクションテスト３", 99999999999))


if __name__ == '__main__':
    unittest.main()
