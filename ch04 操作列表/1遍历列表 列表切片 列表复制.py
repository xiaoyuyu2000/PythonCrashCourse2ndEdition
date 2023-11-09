# Yu Junming
# 09/11/2023
# Chapter 4 操作列表
# 《Python编程从入门到实践》


# 遍历列表
gods = ['Xie Lian', 'Feng Xin', 'Mu Qing', 'Ling Wen']
for god in gods:
    print(f"{god} is in Upper Heaven.")
    print(f"I used to pray for you, {god}.\n")

# Practice 1 2
# 1
pizza = ['Pizza Hut', '101 Pizza', '做披萨的奇葩']
for pizza in pizza:
    print(f"I like {pizza}.")
print("I really love pizza!\n")
# 2
animals = ['cat', 'dog', 'rabbit']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!\n")


# 创建数值列表: range(a, b) - - 创建一个[a, b)的列表
for value in range(1, 5):
    print(value)
# range(a) - - 创建一个[0, a)的列表
for value in range(2):
    print(value)

# list(range(a, b)) - - 生成列表
numbers = list(range(1, 6))
print(numbers)
# range(a, b, c) - - c为步长
numbers = list(range(1, 10, 3))
print(numbers)  # [1, 4, 7]


# example: 创建一个列表包括1~10的平方
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# OR:
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# OR: (列表解析)
squares = [value ** 2 for value in range(1, 11)]
print(squares)


# min(列表), max(列表), sum(列表)
print(min(squares))
print(max(squares))
print(sum(squares))


# Practice 3456789
# 3.
for value in range(1, 21):
    print(value)
# 4.
million_list = list(range(1, 1_000_001))
# for value in million_list:
#     print(value)
print(min(million_list))
print(max(million_list))
print(sum(million_list))
# 6.
odd_list = list(range(1, 21, 2))
for value in odd_list:
    print(value)
# 7.
list_1 = list(range(3, 31, 3))
for value in list_1:
    print(value)
# 8.
numbers = []
for value in range(1, 11):
    numbers.append(value ** 3)
for value in numbers:
    print(value)
# 9.
numbers = [value ** 3 for value in range(1, 11)]
for value in numbers:
    print(value)


# 使用列表的一部分
# 切片
# 列表[a:b:x] - - 输出[a, b)里的元素, 步长为x（默认为1）
gods = ['Xie Lian', 'Feng Xin', 'Mu Qing', 'Ling Wen']
print(gods[0:2])  # 从索引0开始，到索引1
print(gods[1:2])  # 从索引1开始，到索引1
print(gods[:2])    # 从头开始，到索引1
print(gods[1:])    # 从索引1开始，到结束
print(gods[-3:])   # 选择最后3个

# 遍历切片
print("Here are the first three gods in the list:")
for god in gods[:3]:
    print(god)

# 复制列表：创建一个包含整个列表的切片 - - [:]
gods_2 = gods[:]
print(gods_2)

# Practice 10 11 12
# 10.
gods = ['Xie Lian', 'Feng Xin', 'Mu Qing', 'Ling Wen', 'Pei Ming']

print("The first three items in the list are:")
for god in gods[:3]:
    print(god)

print("Three items from the middle of the list are:")
for god in gods[1:4]:
    print(god)

print("The last three items in the list are:")
for god in gods[-3:]:
    print(god)

# 11.
pizzas = ['Pizza Hut', '101 Pizza', '做披萨的奇葩']
friend_pizzas = pizzas[:]
pizzas.append('你猜')
friend_pizzas.append('另一种披萨')
print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

