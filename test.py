import sys
import unittest
import os
current_dir = os.path.dirname(__file__)
app_path = os.path.abspath(os.path.join(current_dir, '..', 'app'))
sys.path.append(app_path)
from main import function

class TestDumbCode(unittest.TestCase):
    def test_dumb1(self):
        self.assertEqual(function(2, 2), 4)
    def test_dumb2(self):
        self.assertEqual(function(1, 2), 1)
    def test_dumb3(self):
        self.assertEqual(function(2, 3), 8)
    def test_dumb4(self):
        self.assertFalse(function(2, 3) == 7)
        
if __name__ == '__main__':
    unittest.main()
