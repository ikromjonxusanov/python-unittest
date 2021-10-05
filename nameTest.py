import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name("ikromjon", "Xusanov")
        self.assertEqual(name, "Ikromjon Xusanov")
    def test_toliq_ism_otasi(self):
        name = get_full_name("ikromjon", "xusanov", 'erkinovich')
        self.assertEqual(name, "Ikromjon Erkinovich Xusanov")


if __name__ == '__main__':
    unittest.main()
