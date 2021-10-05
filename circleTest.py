import unittest
from circle import getArea, getPerimeter

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertEqual(getArea(10), 314.159)
        self.assertEqual(getArea(3), 28.27431)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)

if __name__ == '__main__':
    unittest.main()
