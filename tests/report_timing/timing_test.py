import unittest
import os
import filecmp

class TestingFile(unittest.TestCase):
    def test_case1(self):
        golden_out='golden_out.json'
        actual_out = 'timing_out.json'
        print(filecmp.cmp( golden_out, actual_out))
        self.assertEqual((filecmp.cmp( golden_out, actual_out)),True)
if __name__=='__main__':
    unittest.main()