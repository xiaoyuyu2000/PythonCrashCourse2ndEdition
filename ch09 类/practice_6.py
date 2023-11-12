# Yu Junming
# 12/11/2023
# chapter 9 类  practice 6
# 《Python编程从入门到实践》


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


class IceCreamStand(Restaurant):
    """冰淇淋小店是Restaurant类的子类。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性。"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'strawberry', 'apple']

    def show_flavors(self):
        print("There are following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


icecream = IceCreamStand('Icy', 'sweet food')
icecream.describe_restaurant()
icecream.show_flavors()