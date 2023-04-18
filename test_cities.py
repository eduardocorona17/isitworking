import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests for city_country.py"""
    def test_city_country(self):
        formatted_city = city_country('ushuaia', 'argentina')
        self.assertEqual(formatted_city, 'Ushuaia, Argentina')

    def test_city_country_population(self):
        """Tests with third parameter."""
        formatted_city = city_country('ushuaia', 'argentina', 45000000)
        self.assertEqual(formatted_city, 'Ushuaia, Argentina - Population 45000000')


if __name__ == '__main__':
    unittest.main()