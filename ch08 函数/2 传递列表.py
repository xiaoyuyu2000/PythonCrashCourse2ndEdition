# Yu Junming
# 12/11/2023
# chapter 8 函数  2. 传递列表
# 《Python编程从入门到实践》


def greet_users(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止。打印每个设计后，都将它转移到列表completed_models中。"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)


# 禁止函数修改列表
# 可以选择向函数传递一个原先列表的副本
# print_models(unprinted_models[:], completed_models)


# Practice 9 10 11
# 9.
def show_messages(messages):
    for message in messages:
        print(message)


msgs = ['Good morning!', 'Good afternoon!', 'Good evening!']
show_messages(msgs)


# 10.
def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: '{current_message}'")
        sent_messages.append(current_message)

    print("\nThe following messages have been sent:")
    for message in sent_messages:
        print(message)


msgs = ['Good morning!', 'Good afternoon!', 'Good evening!']
completed_msgs = []
send_messages(msgs, completed_msgs)


# 11.
msgs = ['Good morning!', 'Good afternoon!', 'Good evening!']
completed_msgs = []
send_messages(msgs[:], completed_msgs)
print(msgs)


# 传递任意数量的实参 - - *形参名
# 不论收到几个实参，都可以正常运行
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    """概述要制作的比萨。"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 将位置实参、任意数量实参结合在一起使用
# 任意数量实参，必须放在后面
def make_pizza(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参 - - **实参名
# 用于不确定传递给函数的信息会是什么样的
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


# Practice 12 13 14
# 12.
def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich('mushrooms')
make_sandwich('carrot', 'mushrooms')


# 13.
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile('Junming', 'Yu',
              location='Dalian',
              gender='female',
              country='China')
print(my_profile)


# 14.
def build_car(brand, size, **car_info):
    """建立一个字典用于保存一辆汽车的各种信息。"""
    car_info['brand'] = brand
    car_info['size'] = size
    return car_info


my_car = build_car('bwm', 'outback',
                   color='blue',
                   tow_package=True)
print(my_car)
