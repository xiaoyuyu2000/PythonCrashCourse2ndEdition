# Yu Junming
# 10/11/2023
# Chapter 5 if语句
# 《Python编程从入门到实践》


ghosts = ['qi rong', 'hua cheng', 'he xuan', 'bai wuxaing']
for ghost in ghosts:
    if ghost == 'qi rong':
        print(ghost.upper())
    else:
        print(ghost.title())

# and or
a, b = 10, 15
print(a > 0 and b > 0)  # True
print(a < 0 or b < 0)   # False
numbers = list(range(1, 11, 3))  # [1, 4, 7, 10]
print(a in numbers)     # True
print(b not in numbers)     # True


# Practice 1 2
# 1.
ghost = 'hua cheng'
print("Is ghost == 'hua cheng'? I predict True.")
print(ghost == 'hua cheng')

print("\nIs ghost == 'he xuan'? I predict False.")
print(ghost == 'he xuan', '\n')

# 2.
a, b = 'windy', 'sunny'
print(a == b)
print(a.lower() != b.lower())
print(3 > 0 and 5 < 1)
print(3 > 0 or 5 < 1)
weathers = [a, b]
print('windy' in weathers)
print('sunny' not in weathers)


# if-else
age_1 = 23
age_2 = 17
ages = [age_1, age_2]
for age in ages:
    if age >= 18:
        print("You are old enough to vote!")
        print("Have you registered to vote yet?")
    else:
        print("You are too young to vote!")


# if-elif-else
age_3 = 5
ages.append(age_3)
for age in ages:
    if age >= 18:
        print("Your admission cost is $40.")
    elif age >= 6:
        print("Your admission cost is $24.")
    else:
        print("Your admission cost is $0.")


# Practice 34567
# 3.
alien_color = 'yellow'
if alien_color == 'green':
    print("You have earned 5 points.")
elif alien_color == 'yellow':
    print("You have earned 10 points.")
elif alien_color == 'red':
    print("You have earned 15 points.")

# 6.
age = 10
if age < 2:
    print("This is a baby.")
elif age < 4:
    print("This is a toddler.")
elif age < 13:
    print("This is a child.")
elif age < 20:
    print("This is a teenager.")
elif age < 65:
    print("This is an adult.")
elif age >= 65:
    print("This is an elderly.")

# 7.
favourite_fruits = ['banana', 'watermelon', 'lemon']
if 'banana' in favourite_fruits:
    print("You really like bananas!")
if 'lemon' in favourite_fruits:
    print("You really like lemons!\n")


# if 处理列表
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!\n")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!\n")

# 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


# Practice 8 9 10 11
# 8.
users = ['RR', '16470', 'ml', 'xiaola1220', 'admin']
# users.clear()
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 10.
current_users = ['RR', '16470', 'ml', 'xiaola1220', 'admin']
new_users = ['Rr', 'abc', 'ydw', 'sqx', '89000']

current_users_copy = []
for current_user in current_users:
    current_users_copy.append(current_user.lower())
print(current_users_copy)
for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f"'{new_user}' have been used, please use another name.")
    else:
        print(f"The name '{new_user}' haven't been used yet.")

# 11.
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")