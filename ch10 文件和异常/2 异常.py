# Yu Junming
# 14/11/2023
# chapter 10 文件和异常  2 异常
# 《Python编程从入门到实践》


# try-except
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# 避免崩溃 - - try-except-else代码块
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSeconde number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")


# 分析文本
filename = 'text_files/The Adventures of Sherlock Holmes.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} doesn't exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


def count_words(filename):
    """计算一个文件大概有多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = 'text_files/The Adventures of Sherlock Holmes.txt'
count_words('hiii')
count_words(filename)


# 静默失败 - - 在出现异常时什么都不做 - - pass
try:
    print(5/0)
except ZeroDivisionError:
    pass
else:
    print('hahaha')


# Practice 6 7 8 9 10
# 6.
while True:
    print("Enter two numbers, and I will return the sum of them.")
    print("Enter 'q' to quit.")

    num_1 = input("First number: ")
    if num_1 == 'q':
        break
    num_2 = input("Second number: ")
    if num_2 == 'q':
        break

    try:
        sum = int(num_1) + int(num_2)
    except ValueError:
        print("You should enter a number!")
    else:
        print(f"The sum of {num_1} and {num_2} is {sum}.")


# 8.
file_cat = 'text_files/cats.txt'
file_dog = 'text_files/dogs.txt'
try:
    with open(file_cat, encoding='utf-8') as file_1:
        cats = file_1.readlines()
    with open(file_dog, encoding='utf-8') as file_2:
        dogs = file_2.readlines()
except FileNotFoundError:
    print("The file does not exist.")
else:
    for cat in cats:
        print(cat.rstrip())
    for dog in dogs:
        print(dog.rstrip())
