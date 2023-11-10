# Yu Junming
# 10/11/2023
# chapter 7 用户输入和while循环 - 3. while循环处理列表和字典
# 《Python编程从入门到实践》


# 将元素在列表之间移动
alive_characters = ['shi wudu', 'qi rong']
dead_characters = []

while alive_characters:
    current_character = alive_characters.pop()
    print(f"{current_character.title()} is going to die.")
    dead_characters.append(current_character)

print("\nThe following characters are dead:")
for character in dead_characters:
    print(character.title())


# 删除列表中所有的等于某个特定值的元素
pets = ['dog', 'cat', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)


# 使用用户输入来填充字典
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat's your name?")
    response = input("Which city do you want to visit someday?")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")


print()


# Practice 8 9 10
# 8.
sandwich_orders = ['chicken sandwich', 'salted fish sandwich', 'beef sandwich']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
print("I have made some sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

# 9.
sandwich_orders = ['chicken sandwich', 'salted fish sandwich', 'beef sandwich', 'pastrami', 'pastrami', 'pastrami']
print("\nWe are out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)


# 10.
polling_active = True
places = {}
while polling_active:
    name = input("\nWhat's your name? ")
    place = input("If you could visit one place in the world, where would you go?")
    places[name] = place

    repeat = input("Enter 'quit' to end the program.")
    if repeat == 'quit':
        polling_active = False

print("\n--- The Result ---")
for name, place in places.items():
    print(f"{name} would love to go to {place}.")






