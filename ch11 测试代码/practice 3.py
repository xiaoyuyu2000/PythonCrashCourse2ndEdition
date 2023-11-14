# Yu Junming
# 14/11/2023
# chapter 11 测试代码  practice 3
# 《Python编程从入门到实践》


import unittest


class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = int(salary)

    def give_raise(self, raise_salary=5000):
        self.salary += raise_salary


class TestEmployee(unittest.TestCase):
    def setUp(self):
        """创建一个Employee对象。"""
        self.my_employee = Employee('Mary', 'Greenland', 4000)

    def test_give_default_raise(self):
        """测试默认值涨工资。"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 9000)

    def test_give_custom_raise(self):
        """测试自定义值涨工资。"""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary, 14000)


if __name__ == '__main__':
    unittest.main()