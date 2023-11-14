# Yu Junming
# 12/11/2023
# chapter 10 文件和异常  1 文件读写
# 《Python编程从入门到实践》


# open(文件名字符串) - - 打开文件
# with保证在不需要访问文件后将它关闭，也可以用open()与close()
# read() - - 读取文件对象中的数据

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)


# 文件路径
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)


# 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# 创建一个列表，包含每一行的内容 - - readlines()
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())
print(lines)


pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))


pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)


# Practice 1 2
# 1.
filename = 'text_files/learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())


# 2.
python_string = []
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    new_line = line.replace('Python', 'C')
    python_string.append(new_line)
for line in python_string:
    print(line.rstrip())


# 写入文件
# 写入空文件 - - open(文件名, 'w') - 会覆盖原有内容
# 'w' - 写入  'a' - 附加  'r+' - 读写
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")

# 附加到文件（'a'）
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

with open(filename, 'r+') as file_object:
    contents = file_object.read()
print(contents)


# Practice 3 4 5
# 3.
filename = 'text_files/guest.txt'
while True:
    message = "Please enter your name: "
    message += "\n(Enter 'quit' to quit.)"
    username = input(message)
    if username == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{username}\n")
print("The guest list: ")
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(f"- {line.rstrip()}")


# 4.
