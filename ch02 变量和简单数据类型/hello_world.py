# Yu Junming
# 09/11/2023

print("Hello Python world!")

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

# Practice
# 1.
message_1 = "I miss u."
print('\n' + message_1)
# 2.
message_2 = "I love u."
print(message_2)
message_2 = "But who are u exactly?"
print(message_2)

"This is a String."
'This is also a String.'

print("The language 'Python' is named after Monty Python, not the snake.")

# 字符串的方法title() - 首字母大写
name = "alice wang"
print(name.title())

# upper(), lower()
print(name.upper())
print(name.lower())

# f字符串(f - format)
first_name = "alice"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Good morning, {full_name.title()}! How are you doing?")

message = f"{first_name.title()}, please."
print(message)


# 删除空白：rstrip()
favourite_language = 'python  '
favourite_language = favourite_language.rstrip()
print(f"My favourite language is {favourite_language}.")

# lstrip()：删除左边的空白  strip()：同时删除左右两边的空白
favourite_language = "   python    "
print(favourite_language.lstrip())
print(favourite_language.rstrip())
print(favourite_language.strip())

# Practice 3~7
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)
print(name.upper())
print(name.lower())
# 5.
name = "albert einstein"
message = "A person who never made a mistake never tried anything new."
print(f'{name.title()} once said, "{message}"')
# 7.
name = "\tJix\t\n"
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())


# 数字
print(3 ** 3)  # 27
print(10 ** 3) # 1000
print(3 * 1.0)
print(3.2 + 1.2)
universe_age = 14_000_000_000
print(f"Universe Age = {universe_age}")

# 同时给多个变量赋值
x, y, z = 1, 2, 3
print(x, y, z)

# 常量 - 字母全部大写
MAX_CONNECTIONS = 5000

# Practice
print(1 + 7)
print(10 - 2)
print(2 * 4)
print(8 / 1)
favourite_number = 7
print(f"fMy favourite number is {favourite_number}")


# Python之禅
import this
