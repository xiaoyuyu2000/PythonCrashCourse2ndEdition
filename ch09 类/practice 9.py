# Yu Junming
# 12/11/2023
# chapter 9 类  practice 9
# 《Python编程从入门到实践》


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
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Filling gas now.")


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """先初始化父类的属性，然后初始化电动汽车特有的属性。"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """打印一条消息描述电瓶容量。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """电动汽车不需要油箱。"""
        print("This car doesn't need a gas tank!")


my_car = ElectricCar('特斯拉', '型号A', 2023)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()


