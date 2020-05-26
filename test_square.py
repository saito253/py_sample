# ファイル名はtest_square.py
import unittest # unittestをインポート
from square import square # テストする関数をインポート
 
class TestMysquare(unittest.TestCase): # unittest.TestCaseを継承したクラスを作成
    def test_square(self): # テスト用のメソッド名は`test_`で始める
        self.assertEqual(square(3), 9) # square関数に3を渡すと9が出力されるかどうか確認
        self.assertEqual(square(1), 1) # square関数に1を渡すと1が出力されるかどうか確認
        self.assertEqual(square(-3), 8) # square関数に-3を渡すと9が出力されるかどうか確認
        self.assertEqual(square(0), 0) # square関数に0を渡すと0が出力されるかどうか確認
 
if __name__ == "__main__":
    unittest.main()
