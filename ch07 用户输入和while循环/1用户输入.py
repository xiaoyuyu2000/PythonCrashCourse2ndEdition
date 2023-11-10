# Yu Junming
# 10/11/2023
# chapter 7 用户输入和while循环 - 1. 用户输入
# 《Python编程从入门到实践》


# 函数input()
# name = input("What's your name?\n")
# print(f"Good afternoon, {name}!")

# 超过一行的提示
# prompt = "If you tell us who you are, wo can personalize the messages you see."
# prompt += "\nWhat's your first name?"
#
# name = input(prompt)
# print(f"\nHello, {name}!")


# int() - - 转换为int数值
# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
#     print("You are an adult.")


# Practice 123
# 1.
# car = input("What brand of car do you want to buy? ")
# print(f"Let me see if I can find you a {car}.")

# 2.
# numbers = input("How many people are there going to be? ")
# numbers = int(numbers)
# if numbers > 8:
#     print("There's no more tables available.")
# elif numbers <= 8:
#     print("There are available tables.")

# 3.
number = input("Enter an integer please: ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} divided by 10 leaves {number % 10}.")

