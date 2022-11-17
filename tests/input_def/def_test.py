import unittest
import io
from def_parser import parse_def

class TestingFile(unittest.TestCase):
    def test_case1(self):
        golden_out='golden_out.json'
        actual_out = parse_def('dd1.def', 'def_out.json')
        print(actual_out, "###########")
        self.assertListEqual(
                            list(io.open(golden_out)),
                            list(io.open(actual_out))
                            )
if __name__=='__main__':
    unittest.main()