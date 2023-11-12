# Yu Junming
# 12/11/2023
# chapter 9 类  1. 定义类 初始化 方法
# 《Python编程从入门到实践》


class Dog:
    """一次模拟小狗的简单尝试。"""

    def __init__(self, name, age):
        """初始化属性name和age。"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下。"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚。"""
        print(f"{self.name} rolled over!")


# 特殊方法__init__() - - 两个下划线
# 每当创建一个类对象时，都会自动运行__init__()方法，name和age为属性


# 创建实例
my_dog = Dog('Lisa', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Amy', 10)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")


# Practice 1 2 3
# 1.
class Restaurant:
    """一次模拟餐馆的简单尝试。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化描述餐馆的属性。"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐馆的属性。"""
        print(f"\nThe restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        """餐馆正在营业。"""
        print(f"{self.restaurant_name} is now opening.")


a_restaurant = Restaurant('KFC', 'fastfood')
a_restaurant.describe_restaurant()
a_restaurant.open_restaurant()

# 2.
b_restaurant = Restaurant('McDonald', 'fastfood')
c_restaurant = Restaurant('Pizza Hut', 'fastfood')
b_restaurant.describe_restaurant()
c_restaurant.describe_restaurant()


# 3.
class User:
    """模拟一个用户类。"""

    def __init__(self, first_name, last_name, age):
        """初始化描述用户的属性。"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """描述用户的信息。"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")

    def greeting_user(self):
        """问候用户。"""
        print(f"Hi, {self.first_name.title()} {self.last_name.title()}!")


user_1 = User('Junming', 'Yu', 23)
user_1.describe_user()
user_1.greeting_user()
user_2 = User('Amy', 'Smith', 10)
user_2.describe_user()
user_2.greeting_user()


# 给属性指定默认值
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# 修改属性的值
# 1. 直接修改
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# 2. 通过方法修改
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值。并且禁止回调里程数。"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()
my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_new_car.update_odometer(22)


# Practice 4 5
# 4.
class Restaurant:
    """一次模拟餐馆的简单尝试。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化描述餐馆的属性。"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆的属性。"""
        print(f"\nThe restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
        print(f"Customers visited: {self.number_served}")

    def open_restaurant(self):
        """餐馆正在营业。"""
        print(f"{self.restaurant_name} is now opening.")

    def set_number_serverd(self, customers):
        """设置就餐人数。"""
        self.number_served = customers

    def increment_number_served(self, customers):
        """增加就餐过的人数。"""
        self.number_served += customers


kfc = Restaurant('KFC', 'fastfood')
kfc.describe_restaurant()

kfc.set_number_serverd(55)
kfc.describe_restaurant()

kfc.increment_number_served(10)
kfc.describe_restaurant()


# 5.
class User:
    """模拟一个用户类。"""

    def __init__(self, first_name, last_name, age):
        """初始化描述用户的属性。"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """描述用户的信息。"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")

    def greeting_user(self):
        """问候用户。"""
        print(f"Hi, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """将登录次数增加一次。"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将登录次数重置为0。"""
        self.login_attempts = 0


rr = User('Junming', 'Yu', 23)
rr.describe_user()
rr.greeting_user()
rr.increment_login_attempts()
rr.increment_login_attempts()
rr.increment_login_attempts()
print(rr.login_attempts)
rr.reset_login_attempts()
print(rr.login_attempts)