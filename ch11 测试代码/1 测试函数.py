# Yu Junming
# 14/11/2023
# chapter 11 测试代码  1 测试函数
# 《Python编程从入门到实践》


# 测试：引入模块unittest
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py。"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的名字吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的名字吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
