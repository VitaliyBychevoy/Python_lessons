import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):

    # def test_city_country(self):
    #     city_and_country = city_country("santiago", 'chile')
    #     self.assertEqual(city_and_country, "Santiago, Chile")

    def test_city_country_population(self):
        city_and_country = city_country("santiago", 'chile', '5 000 000')
        self.assertEqual(city_and_country, "Santiago, Chile - population 5 000 000")


if __name__ == '__main__':
    unittest.main()