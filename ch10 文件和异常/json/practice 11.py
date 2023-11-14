# Yu Junming
# 14/11/2023
# chapter 10 文件和异常  practice 11
# 《Python编程从入门到实践》
import json


def get_number():
    """读取用户输入的喜欢的数字。"""
    number = input("What's your favourite number? ")
    filename = 'favourite_number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number


def get_stored_number():
    """从文件中读取用户输入过的最喜欢的数字。"""
    filename = 'favourite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def favourite_number():
    """告诉用户记得对方最喜欢的数字，或是提示输入最喜欢的数字。"""
    number = get_stored_number()
    if number:
        print(f"I know your favourite number! It's {number}.")
    else:
        number = get_number()
        print(f"I will remember your number {number} when you come back.")


favourite_number()