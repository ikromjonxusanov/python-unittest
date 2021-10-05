import unittest
from car import Car

class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        make = "kia"
        model = "k5"
        year = 2021
        self.price = 40000
        self.km = 10000
        self.auto1 = Car(make, model, year)
        self.auto2 = Car(make, model, year, price=self.price)
    def test_create(self):
        self.assertIsNotNone(self.auto1.make)
        self.assertIsNotNone(self.auto1.model)
        self.assertIsNotNone(self.auto1.year)
        self.assertIsNone(self.auto1.price)
        self.assertEqual(0, self.auto1.get_km())
        self.assertEqual(40000, self.auto2.price)
    def test_set_price(self):
        self.auto1.set_price(self.price)
        self.assertEqual(self.price, self.auto1.price)
    def test_add_km(self):
        self.auto1.add_km(self.km)
        self.assertEqual(self.km, self.auto1.get_km())
        new_km = -5000
        try:
            self.auto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

    def test_get_info(self):
        avto1_info = 'KIA K5, 2021-yil, 0km yurgan.'
        self.assertEqual(avto1_info, self.auto1.get_info())
        # avto1 narhi va km o'zgartiramiz
        self.auto1.set_price(50000)
        self.auto1.add_km(20000)
        avto1_info = 'KIA K5, 2021-yil, 20000km yurgan. Narxi: 50000'
        self.assertEqual(avto1_info,self.auto1.get_info())



if __name__ == '__main__':
    unittest.main()
