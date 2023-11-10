# Yu Junming
# 10/11/2023
# Chapter 6 字典 - 3. 嵌套
# 《Python编程从入门到实践》


# 字典组成的列表

# 创建一个用于存储ghost的空列表
ghosts = []

# 创建30个黑色的ghost
for ghost_number in range(30):
    new_ghost = {'color': 'black', 'points': 5, 'speed': 'slow'}
    ghosts.append(new_ghost)

# 显示前5个ghost
for ghost in ghosts[:5]:
    print(ghost)
print("...")

# 显示一共创建了多少个ghost
print(f"Total number of ghosts: {len(ghosts)}")


# 修改
for ghost in ghosts[:3]:
    if ghost['color'] == 'black':
        ghost['color'] = 'green'
        ghost['speed'] = 'medium'
        ghost['points'] = 10

# 显示前5个ghost
# 显示前5个ghost
for ghost in ghosts[:5]:
    print(ghost)
print("...")


# 字典中的列表
hx = {
    'kind': 'ghost',
    'friends': ['hua cheng', 'shi qingxuan']
}
print(f"HX is a {hx['kind']} whose friends are: ")
for friend in hx['friends']:
    print(f"\t{friend.title()}")


friends = {
    'he xuan': ['hua cheng', 'shi qingxuna'],
    'shi qingxuan': ['ming yi', 'xie lian'],
    'xie lian': ['san lang', 'shi qingxuna'],
}
for name, friend in friends.items():
    print(f"{name.title()}'s friends are: ")
    for friend_name in friend:
        print(f"\t{friend_name.title()}")


# 字典中的字典
ghosts = {
    'qi rong': {
        'title': '青灯夜游',
        'color': 'green',
        'state': '凶'
    },

    'he xuan': {
        'title': '黑水沉舟',
        'color': 'black',
        'state': '绝'
    },

    'hua cheng': {
        'title': '血雨探花',
        'color': 'red',
        'state': '绝'
    },

    'bai wuxiang': {
        'title': '白衣祸世',
        'color': 'white',
        'state': '绝'
    },
}

for ghost, ghost_info in ghosts.items():
    print(f"\nName: {ghost.title()}")
    for key, value in ghost_info.items():
        print(f"\t{key.title()}: {value}"

)


# Practice 7 ~ 12
# 7.
person_1 = {
    'age': 23,
    'city': 'Dalian'
}
person_2 = {
    'age': 25,
    'city': 'Shanghai'
}
person_3 = {
    'age': 22,
    'city': 'Yangzhou'
}
people = {
    'RR': person_1,
    '猫猫': person_2,
    'swallow': person_3
}

for person, person_info in people.items():
    print(f"name: {person}")
    for key, value in person_info.items():
        print(f"\t{key}: {value}")

# 8.
pets = [
    {'dog': 'Lily'},
    {'cat': 'Amy'}
]
for pet in pets:
    for kind, name in pet.items():
        print(f"This {kind} belongs to {name}.")

# 9.
favourite_places = {
    'he xuan': ['黑水岛', '博古镇', '地师殿'],
    'shi qingxuan': ['风水殿', '皇城'],
    'xie lian': ['菩荠观', '极乐坊']
}
for person, favourite_place in favourite_places.items():
    print(f"{person.title()}'s favourite places:")
    for place in favourite_place:
        print(f"\t{place}")

# 11.
cities = {
    'dalian': {
        'country': 'China',
        'population': 608_0000,
        'establish': 1899
    },
    'paris': {
        'country': 'France',
        'population': 1200_0000,
        'establish': -250
    },
    'new york': {
        'country': 'America',
        'population': 880_0000,
        'establish': 1624
    }
}
for city, city_info in cities.items():
    print(f"Name: {city.title()}")
    for key, value in city_info.items():
        print(f"\t{key.title()}: {value}")
