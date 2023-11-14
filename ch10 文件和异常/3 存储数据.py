# Yu Junming
# 14/11/2023
# chapter 10 文件和异常  3 存储数据
# 《Python编程从入门到实践》


# 使用JSON模块，将数据结构存储到文件中
# JSON（JavaScript Object Notation）

# json.dump() - - 存储数据
# json.load() - - 读取数据

import json

numbers = [2, 3, 4, 7, 11, 13, 15]

filename = 'json/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers_read = json.load(f)
print(numbers_read)


# 保存和读取用户输入的数据

# 如果以前存储了用户名就加载它，否则提示用户输入用户名并存储它
# filename = 'json/username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We will remember you when you come back, {username}!")
# else:
#     print(f"Welcome back, {username}!")


def get_stored_username():
    """如果存储了用户名，就获取它。"""
    filename = 'json/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_user():
    """提示输入用户名。"""
    username = input("What is your name? ")
    filename = 'json/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其名字。"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_user()
        print(f"We will remember you when you come back, {username}!")


greet_user()


