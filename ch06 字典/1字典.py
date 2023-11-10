# Yu Junming
# 10/11/2023
# Chapter 6 字典 - 1. 字典
# 《Python编程从入门到实践》


# 字典，是一系列键值对，用花括号{}
sqx = {'racist': 'god', 'status': 'alive'}
hx = {'racist:': 'ghost', 'status': 'dead', 'color': 'black'}
print(sqx)
print(hx)

# 访问值
print(f"HX's color is {hx['color']}.")
print(f"SQX is {sqx['status']}.")

# 添加键值对
sqx['color'] = 'green'
print(sqx)

# 修改字典中的值
sqx['color'] = 'white'
print(sqx)

# 删除键值对
del sqx['color']
print(sqx)

# 较长的字典
favourite_colors = {
    'xie lian': 'white',
    'hua cheng': 'red',
    'he xuan': 'black',
    'shi qingxuan': 'green'
}
print(favourite_colors)


# 使用get()访问值
# get(键, 如果键不存在则返回的值)
print(favourite_colors.get('qi rong', "No idea."))


# Practice 1 2 3
# 1.
person = {
    'first_name': 'Junming',
    'last_name': 'Yu',
    'age': 23,
    'city': 'Dalian'
}
print(person)

# 2.
favourite_numbers = {
    'RR': 7,
    'ml': 8,
    'abc': 10,
    'lily': 1,
    'nobody': 0
}
print(f"RR's favourite number is {favourite_numbers['RR']}.")
print(f"ml's favourite number is {favourite_numbers['ml']}.")
print(f"abc's favourite number is {favourite_numbers['abc']}.")
print(f"lily's favourite number is {favourite_numbers['lily']}.")
print(f"nobody's favourite number is {favourite_numbers['nobody']}.")

# 3.
vocabulary = {
    'list': '列表',
    'tuple': '元组',
    'key': '键',
    'value': '值',
    'function': '函数'
}
print(f"list:\n\t{vocabulary['list']}")
print(f"tuple:\n\t{vocabulary['tuple']}")
print(f"key:\n\t{vocabulary['key']}")
print(f"value:\n\t{vocabulary['value']}")
print(f"function:\n\t{vocabulary['function']}")



