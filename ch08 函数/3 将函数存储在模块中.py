# Yu Junming
# 12/11/2023
# chapter 8 函数  3. 将函数存储在模块中
# 《Python编程从入门到实践》


# import语句引入模块，调用pizza.py中的make_pizza()函数
# pizza.py
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入特定的函数
# from 模块名 import 函数1,函数2,函数3
from pizza import greeting

greeting()


# 使用as给函数指定别名
# from MODULE_NAME import FUNCTION_NAME as NAME
from pizza import greeting as print_hi

print_hi()


# 使用as给模块指定别名
# import MODULE as NAME
import pizza as my_pizza
my_pizza.make_pizza(10, 'guess')


# 导入模块中的所有函数
# from MODULE import *
from pizza import *
# 但最好是只导入需要的函数，或者导入整个模块并使用句点表示法


# Practice 15 16 17
# 15.
from printing_functions import print_models
models = ['apple', 'car', 'buildings']
finished_models = []
print_models(models[:], finished_models)
