# Yu Junming
# 10/11/2023
# chapter 7 用户输入和while循环 - 2. while循环
# 《Python编程从入门到实践》


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1     # 1 2 3 4 5


# 让用户选择何时退出循环
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
#     elif message == 'quit':
#         print("Bye!")


# 使用标志(flag)
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
#
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#         print("---Bye---")
#     else:
#         print(message)


# 使用break退出循环
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

print()

# 循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)       # 1 3 5 7 9


# Practice 4567
# 4.
# prompt = "\n请输入一系列披萨配料:"
# prompt += "\n输入'quit'结束。"
#
# while True:
#     pizza = input(prompt)
#     if pizza == 'quit':
#         print("请稍等~")
#         break
#     else:
#         print(f"您的{pizza}会被添加~")

# 5.
# message = "\nHow old are you? "
# message += "\nEnter 'quit' to end the program."
#
# while True:
#     age = input(message)
#     price = ""
#     if age == 'quit':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age < 12:
#             price = 10
#         elif age >= 12:
#             price = 15
#
#         print(f"The price of you is ${price}.")


# 6.
# 1: while
# message = "\nHow old are you? "
# message += "\nEnter 'quit' to end the program."
#
# age = ""
# price = ""
# while age != 'quit':
#     age = input(message)
#     if age != 'quit':
#         age = int(age)
#
#         if age < 3:
#             price = 0
#         elif age < 12:
#             price = 10
#         elif age >= 12:
#             price = 15
#         print(f"The price of you is ${price}.")

# 2: flag
message = "\nHow old are you? "
message += "\nEnter 'quit' to end the program."

active = True
price = ""
while active:
    age = input(message)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        elif age >= 12:
            price = 15
        print(f"The price of you is ${price}.")