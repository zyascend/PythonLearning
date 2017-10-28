# -*-coding:utf-8-*-
import functools
from functools import reduce

a = "aaaaa"
print(a)
print(a)
a = None
print(a)
print(40 // 6)
a = '中'
print(chr(25598))
a = len(a.encode('utf-8'))
print(a)

# 格式化字符串
a = 'Age: %s. Gender: %s' % (25, True)
print(a)

# list的应用
l = ['aaa', 'bbb', 'ccc']
print(l)
# 末尾添加元素
l.append('ddd')
print(l)
# 指定位置添加元素
l.insert(1, 'eee')
print(l)
# 删除末尾
l.pop()
print(l)
l.pop(1)
print(l)

# list的元素也可以不一样
l = ['aaa', 12, True]
print(l)
l = ['aaa', 12, True, ['a', 'b']]
print(l)

# tuple 不可变的list,tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
l = ('a', 'b', 'c')
print(l)
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义 (1) = 1 (int)
l = (1,)
print(l)
l = (1)
print(l)

age = 55
if age >= 18 and age < 50:
    print('your age is :', age)
    print('adult')
elif age >= 50:
    print('old man')
else:
    print('your age is :', age)
    print('child')

# inputs = input('birth:')
# birth = int(inputs)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# 关于循环
sum = 0
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in l:
    sum += x
print(sum)

sum = 0
for i in range(101):
    sum += i
print(sum)

sum = 0
n = 100
while n > 0:
    sum += n
    n -= 1
print(sum)

# 关于map和set
d = {'aaa': 111, 'bbb': 222, 'ccc': 333}
print(d['aaa'])
print(d.get('aaa'))
print('ddd' in d)

s = {1, 2, 3}
print(s)
s.add(3)
s.add(5)
s.remove(3)
print(s)

# 关于方法调用
print(max(1, 32, 999))
a = max  # a是一个指向函数的引用
print(a(1, 2))


# 定义一个函数(方法)
def my_method(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad type")
    print(x)
    return 'called', "hhhh"  # 可以返回多个返回值（实质是返回一个tuple）


print(my_method(66666))


def my_def_method(x, n=2):  # n 为默认参数必选参数在前，默认参数在后，！！！默认参数必须指向不可变对象
    print(x, n)


my_def_method(666, 3)
my_def_method(666)


def my_more_method(*numbers):
    # 可变参数，相当于传入了一个tuple
    print(numbers)


my_more_method(1, 2, 3, 4)

# def my_other_method(x,y, **other):
#     # 关键字参数，接收一个map
#     print('other = ', other)
#
#
# my_other_method(666,888)
# my_other_method(666,888,{1:2,3:4})


# 切片
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[0:3])
print(l[-1])  # 取倒数
print(l[-3:-1])
print(l[:10:2])  # 前10个，每两个取一个
a = "String"
print(a[-1])  # String也可以切

# 迭代
d = {'a': 1, 'b': 2, 'c': 1}
for k, v in d.items():
    print(k, v)

# 列表生成式
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列表生成器 保存算法，不占内存
g = (x * x for x in range(1, 11))
print(next(g))
print(next(g))


# 最难理解的就是generator和函数的执行流程不一样
# 。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数
# ，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def odd():
    print('step 1')
    yield 1  # return 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


g = odd()  # 生成一个generator
print(next(g))
print(next(g))


# map()处理数据
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
l = list(r)
print(l)
print(list(map(str, [1, 2, 3, 4])))  # list中所有数字转化为字符串


#  reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    return reduce(fn, map(char2num, s))


print(str2int('456'))


# filter筛选数据
def is_odd(n):
    return n % 2 == 0


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

# sort
l = [45, 5, 8, 45, -7, 0]
print(sorted(l))
print(sorted(l, key=abs))  # key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


def count():  # 返回一个方法，且满足闭包
    def f(x):
        def g():
            return x * x

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


#  装饰器


def log(func):
    def wrapper(*arg, **kw):
        print('call %s()' % func.__name__)
        return func(*arg, **kw)

    return wrapper


@log
def now():
    print("2017-10-28")


now()

# 偏函数
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
int2 = functools.partial(int, base=2)
print('---', int2("100011"))
print(functools.partial(max, 10)(1, 2, 3))


#  面向对象
class Student(object):
    def __init__(self, name, score):
        self.score = score
        self.name = name
        self.__sex = 1  # __ 标识此变量为private

    def print_score(self):
        print('score:', self.score)


s1 = Student('MIng', 100)
print(s1)
print('%s : %s' % (s1.name, s1.score))
s1.print_score()
