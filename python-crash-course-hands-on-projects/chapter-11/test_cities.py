# Write a function that accepts two parameters: a city name and a country name. 
# The function should return a single string of the form City, Country , such as 
# Santiago, Chile . Store the function in a module called city _functions.py. 
# Create a file called test_cities.py that tests the function you just wrote 
# (remember that you need to import unittest and the function you want to test). 
# Write a method called test_city_country() to verify that calling your function 
# with values such as 'santiago' and 'chile' results in the correct string. 
# Run test_cities.py, and make sure test_city_country() passes.

import unittest
from city_functions import city_country_one, city_country_two

class NamesTest(unittest.TestCase):
    def test_city_country_one(self):
        name_test = city_country_one("santiago", "chile")
        self.assertEqual(name_test, "santiago, chile")

    def test_city_country_population(self):
        name_test = city_country_two("santiago", "chile", population = "5000000")
        self.assertEqual(name_test, "santiago, chile - population = 5000000")

unittest.main()