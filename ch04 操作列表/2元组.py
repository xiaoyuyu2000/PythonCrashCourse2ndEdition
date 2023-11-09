# Yu Junming
# 09/11/2023
# Chapter 4 操作列表 -  4.5 元组
# 《Python编程从入门到实践》


# 元组 tuple - 不可以修改的列表
# 列表[]    元组()
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Practice 13
print("\nOriginal menu:")
foods = ('糖醋排骨', '松鼠鱼', '酸菜鱼', '泡椒牛蛙', '柠檬汁')
for food in foods:
    print(food)

print("\nModified menu:")
foods = ('糖醋排骨', '椒麻鸡', '酸菜鱼', '泡椒牛蛙', '苹果汁')
for food in foods:
    print(food)

