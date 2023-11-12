# Yu Junming
# 12/11/2023
# chapter 8 函数  1. 定义函数 传递参数 返回字典
# 《Python编程从入门到实践》


# 定义函数
def greet_user():
    """显示简单的问候语。"""
    print("Hello!")


greet_user()


# 向函数中传递信息
# def greet_user(username): - - username - - 形参(parameter)
def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello, {username}!")


# greet_user("RR") - - "RR" - - 实参(argument)
greet_user("RR")


# Practice 1 2
# 1.
def display_message():
    """显示一句话。"""
    print("This chapter is about function in Python.")


display_message()


# 2.
def favourite_book(title):
    """显示一条信息。"""
    print(f"One of my favourite books is {title.title()}.")


favourite_book("harry potter")


# 传递实参（argument）

# 位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('dog', 'Sunny')
describe_pet('cat', 'Miao')


# 关键字实参
describe_pet(pet_name='Jix', animal_type='Goldfish')


# 给形参指定默认值
def describe_pet_2(pet_name, animal_type='cat'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet_2(pet_name='Summer')


# Practice 345
# 3.
def make_shirt(size, logo):
    """显示T恤的尺码和字样。"""
    print(f"The T-shirt's is {size} and the logo is '{logo}'.")


make_shirt(160, 'RR')
make_shirt(size=160, logo='MM')


# 4.
def make_shirt(size, logo="I love Python"):
    """显示T恤的尺码和字样。"""
    print(f"The T-shirt's is {size} and the logo is '{logo}'.")


make_shirt(size=165)
make_shirt(size=180, logo="WTO")


# 5.
def describe_city(city, country="China"):
    """显示一个城市属于某一个国家。"""
    print(f"{city.title()} is in {country.title()}.")


describe_city(city='paris', country='frence')
describe_city(city='shanghai')


# 返回值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


my_name = get_formatted_name('junming', 'yu')
print(my_name)


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# 返回字典
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# 结合函数使用while循环
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名。"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(Enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# Practice 678
# 6.
def city_country(city, country):
    message = f"{city.title()}, {country.title()}"
    return message


city_1 = city_country('dalian', 'china')
city_2 = city_country('paris', 'france')
city_3 = city_country('new york', 'america')
print(city_1)
print(city_2)
print(city_3)


# 7.
def make_album(name, work, songs=None):
    album = {'musician': name, 'album name': work}
    if songs:
        album['songs'] = songs
    return album


album_1 = make_album('Lisa', 'Love Like You')
album_2 = make_album('Hita', 'Losing', 12)
album_3 = make_album('RR', 'Returning Why', 2)
print(album_1)
print(album_2)
print(album_3)


# 8.
while True:
    print("\nPlease enter the info about the albums:")
    print("(Enter 'q' to quit at any time)")

    name = input("The musician's name: ")
    if name == 'q':
        break

    album_name = input("The album's name:")
    if album_name == 'q':
        break

    songs = input("How many songs are there in the album: (Press 'Enter' to skip) ")
    if songs == 'q':
        break

    album = make_album(name, album_name, songs)
    print(f"\n{album}")












