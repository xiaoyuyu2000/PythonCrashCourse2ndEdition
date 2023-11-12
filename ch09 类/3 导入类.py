# Yu Junming
# 12/11/2023
# chapter 9 类  3. 导入类
# 《Python编程从入门到实践》


from car import Car

my_car = Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())

my_car.update_odometer(30)
my_car.read_odometer()

# Python标准库
from random import randint  # randint(a, b) - - 生成[a,b]的随机数

for i in range(4):
    print(randint(1, 6))

from random import choice

fruits = ['apple', 'banana', 'strawberry']
for i in range(4):
    print(choice(fruits))


# Practice 13 14 15 16
# 13.
class Die:
    """创建了一个骰子类。"""

    def __init__(self, sides=6):
        """初始化属性，sides默认为6。"""
        self.sides = sides

    def roll_die(self, times):
        """模拟掷骰子。"""
        print("\nStart:")
        for i in range(times):
            result = randint(1, self.sides)
            print(f"{i + 1}: {result}")


die_6_sides = Die()
die_6_sides.roll_die(10)

die_10_sides = Die(10)
die_10_sides.roll_die(10)

die_20_sides = Die(20)
die_20_sides.roll_die(10)


# 14.
choices = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
prize = 'ab89'
my_ticket = []


def if_win():
    """摇奖的过程。"""
    while True:
        result = ""
        for i in range(4):
            character = choice(choices)
            result += character

        my_ticket.append(result)

        if result == prize:
            print("\nYou won the prize!")
            break


if_win()
print(f"I have tried {len(my_ticket)} times!")




