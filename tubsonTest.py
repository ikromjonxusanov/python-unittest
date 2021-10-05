import unittest
from tubson import tubSon

class TubsonTast(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSon(7))
        self.assertTrue(tubSon(193))
        self.assertTrue(tubSon(547))

    def test_false(self):
        self.assertFalse(tubSon(6))
        self.assertFalse(tubSon(265))
        self.assertFalse(tubSon(489))


if __name__ == '__main__':
    unittest.main()
