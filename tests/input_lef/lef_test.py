import unittest
import os
import filecmp
import io

class TestingFile(unittest.TestCase):
    def test_case1(self):
        golden_out='golden_out.json'
        actual_out = 'lef_out.json'
        
        self.assertListEqual(
                            list(io.open(golden_out)),
                            list(io.open(actual_out))
                            )
if __name__=='__main__':
    unittest.main()