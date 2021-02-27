import random

# ==========================================================
# 范围遍历基础语法
# ==========================================================

# range 范围 开始,停止,步长
# for i in range(0,10,2):
#     print('i ' + str(i))

# range 范围 开始,停止,步长
print('---------范围 开始,停止,步长')
for i in range(5, -1, -1):
    print('i ' + str(i))

print('---------输入1到10随机数')
# 输入1到10随机数
for i in range(5):
    if i == 3:
        break
    print(random.randint(1, 10))

print('---------定义函数')
def hello():
    print('hello')
hello()

print('---------输出全局变量')
def spam():
    print(agg)

agg =23
spam()

print('---------print分隔符')
print('a','b','c',sep='|')

print('---------for循环打印列表')
spam = ['a','b','c']
for c in spam:
    print(c)

print('---------in测试')
if 'a' in spam:
    print('a in spam')

print('---------not in测试')
if 'a1' not in spam:
    print('a1 not in spam')

print('---------append测试')
spam.append('e')
print(spam)

spam.insert(2,'word')
print(spam)