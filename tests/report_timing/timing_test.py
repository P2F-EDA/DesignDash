import unittest
import os
import filecmp
import io
from timing_parser import parse_timing

class TestingFile(unittest.TestCase):
    def test_case1(self):
        golden_out='golden_out.json'
        actual_out = parse_timing('setup.txt', 'timing_out.txt')
        print(actual_out, "###########")
        self.assertListEqual(
                    list(io.open(actual_out)),
                    list(io.open(golden_out))
                    )
        # self.assertEqual((filecmp.cmp( golden_out, actual_out)),True)
if __name__=='__main__':
    unittest.main()