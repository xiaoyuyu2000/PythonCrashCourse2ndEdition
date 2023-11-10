# Yu Junming
# 10/11/2023
# Chapter 6 字典 - 2. 遍历字典
# 《Python编程从入门到实践》


# 遍历字典
# for key, value in 字典.item(): - -key,value可以用任意的名称
favourite_colors = {
    'xie lian': 'white',
    'hua cheng': 'red',
    'he xuan': 'black',
    'shi qingxuan': 'green'
}
for name, color in favourite_colors.items():
    print(f"Name: {name.title()}")
    print(f"Favourite Color: {color}\n")

# 只遍历字典中的键 - -字典.keys() - -也可以省略，因为默认遍历的就是所有键
for name in favourite_colors.keys():
    print(name.title())
# for name in favourite_colors:


# 按特定顺序遍历字典中所有键
for name in sorted(favourite_colors.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# 只遍历字典中的值 - -字典.values()
for color in favourite_colors.values():
    print(color)

# set()对包含重复元素的列表使用，得到一个不包含重复元素的【集合】
favourite_colors = {
    'xie lian': 'white',
    'hua cheng': 'red',
    'he xuan': 'black',
    'shi qingxuan': 'green',
    'qi rong': 'green'
}
print("The following colors have been mentioned:")
for color in set(favourite_colors.values()):
    print(color)
print(set(favourite_colors.values()))  # {'black', 'green', 'red', 'white'} - - 这是一个集合


# Practice 456
# 4.
vocabularies = {
    'list': '列表 - 可重复 []',
    'tuple': '元组 - 类似列表，但不可修改 ()',
    'dictionary': '字典 - 键值对 {}',
    'set': '集合 - 无序，不重复 {}',
}
for vocabulary, explanation in vocabularies.items():
    print(f"{vocabulary}:\n\t{explanation}")

# 5.
rivers = {
    'nile': 'egypt',
    'seine': 'france',
    'yangtze river': 'china',
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)

# 6.
favourite_colors = {
    'xie lian': 'white',
    'hua cheng': 'red',
    'he xuan': 'black',
    'shi qingxuan': 'green',
    'qi rong': 'green'
}
ghosts = ['hua cheng', 'he xuan', 'qi rong', 'ban yue']
for ghost in ghosts:
    if ghost in favourite_colors.keys():
        print(f"I have already known {ghost.title()}'s favourite color.")
    else:
        print(f"I want to know {ghost.title()}'s favourite color.")
        