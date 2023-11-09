# Yu Junming
# 09/11/2023
# Chapter 3 列表简介
# 《Python编程从入门到实践》


# 列表[a, b, c, d]
ghosts = ['QR', 'HX', 'BWX', 'HC']
print(ghosts)

# 访问列表元素
print(ghosts[0])
print(ghosts[0].lower())
print(ghosts[-1])
print(ghosts[-3])

message = f"{ghosts[3]}'s title is Crimson Rain Sought Flower."
print(message)

# Practice 1~3
ghosts_name = ['Qi Rong', 'He Xuan', 'Bai WuXiang', 'Hua Cheng']
for i in ghosts_name:
    print(f"This is {i}.")


# 修改添加删除列表元素
ghosts_name = ['Qi Rong', 'He Xuan', 'Bai WuXiang', 'Hua Cheng']
ghosts_name[2] = 'Jun Wu'
print(ghosts_name)

# 添加: append()
ghosts_name.append('15°')
print(ghosts_name)

# 插入：insert(索引, 值)
ghosts_name.insert(5, 'SQX')
print(ghosts_name)

# 删除：del 列表[索引]
del ghosts_name[5]
print(ghosts_name)

# 删除：pop(索引)
popped_ghosts = ghosts_name.pop()
print(ghosts_name)
print(popped_ghosts)

# 根据值删除：remove(值)
defeat_ghost = 'Jun Wu'
ghosts_name.remove(defeat_ghost)
print(ghosts_name)
print(f"{defeat_ghost} has been knocked out.\n")

# Practice 4567
# 4.
invitee = ['He Xuan', 'Shi QingXuan', 'Xie Lian', 'Hua Cheng']
for i in invitee:
    print(f"Please join me for dinner, {i}.")
# 5.
busy_invitee = invitee.pop(3)
print(f"{busy_invitee} is busy.")
invitee.append('Feng Xin')
for i in invitee:
    print(f"Please join me for dinner, {i}.")
# 6.
print('\nI have found a bigger place for dinner!')
invitee.insert(0, 'Mu Qing')
invitee.insert(3, 'Yin Yu')
invitee.append('Quan YiZhen')
for i in invitee:
    print(f"Please join me for dinner, {i}.")
# 7.
print("\nI'm sorry that I can only invite two of you.")
delete_invitee = invitee.pop(0)
print(f'Sorry, I can not have dinner with you, {delete_invitee}.')
delete_invitee = invitee.pop()
print(f'Sorry, I can not have dinner with you, {delete_invitee}.')
delete_invitee = invitee.pop()
print(f'Sorry, I can not have dinner with you, {delete_invitee}.')
delete_invitee = invitee.pop()
print(f'Sorry, I can not have dinner with you, {delete_invitee}.')
delete_invitee = invitee.pop()
print(f'Sorry, I can not have dinner with you, {delete_invitee}.')
for i in invitee:
    print(f'Please join me for dinner, {i}.')
del invitee[0]
del invitee[0]
print(invitee)


print()



# 组织列表
# 排序（永久）：sort()
ghosts = ['Qi Rong', 'He Xuan', 'Bai WuXiang', 'Hua Cheng']
ghosts.sort()
print(ghosts)

ghosts.sort(reverse=True)
print(ghosts)

# 排序（临时）：sorted(列表)
ghosts = ['Qi Rong', 'He Xuan', 'Bai WuXiang', 'Hua Cheng']
print("\nHere is the original list:")
print(ghosts)
print("Here is the sorted list:")
print(sorted(ghosts))
print("Here is the original list again:")
print(ghosts)

# 倒置：reverse()
ghosts.reverse()
print(ghosts)

# 长度：len()
length = len(ghosts)
print(length)

# Practice 8 9 10
# 8.
dream = ['Paris', 'Denmark', 'Berlin', 'London', 'Munich']
print(dream)
print(sorted(dream))
print(dream)
print(sorted(dream, reverse=True))
print(dream)
dream.reverse()
print(dream)
dream.reverse()
print(dream)
dream.sort()
print(dream)
dream.sort(reverse=True)
print(dream)

# 9.
print(f"There are {len(dream)} cities I want to visit.")









