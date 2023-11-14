# Yu Junming
# 14/11/2023
# chapter 11 Practice 1
# 《Python编程从入门到实践》


import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """测试city_functions.py。"""

    def test_city_country(self):
        """能够正确地处理像santiago, chile这样的值吗？"""
        message = city_country('santiago', 'chile')
        self.assertEqual(message, 'Santiago, Chile')

    def test_city_country_population(self):
        """能够正确地处理带有population属性的信息吗？"""
        message = city_country('santiago', 'chile', 5000000)
        self.assertEqual(message, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
