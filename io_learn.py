# -*-coding:utf-8-*-
import os
import json

print(os.name)
print(os.environ)
# 查看当前目录的绝对路径: E:\PythonProjects
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('E:\PythonProjects', 'newDir'))
# 然后创建一个目录:
# os.mkdir('E:\PythonProjects\\newDir')
# 删掉一个目录:
# os.rmdir('E:\PythonProjects\\newDir')
# 合并路径不要直接拼接string
newPath = os.path.join('old\path', 'new\path')
# 拆分路径时，也不要直接去拆字符串
print(os.path.split('user/path/hello.txt'))  # ('user/path', 'hello.txt')
print(os.path.splitext('user/path/hello.txt'))  # ('user/path/hello', '.txt')
# 对文件重命名:
# os.rename()
# 删掉文件:
# os.remove()
# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 要列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# 序列化
d = dict(name='ZY', age=20, height=178)
jsonString = json.dumps(d)
print(jsonString)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def trans2Dic(self):
    return {
        'name': self.name,
        'score': self.score,
        'age': self.age
    }


# 对象转化为json
s = Student('ZY', 21, 60)
strs = json.dumps(s, default=trans2Dic)
print(strs)


# json转化为对象
def dic2Class(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(strs, object_hook=dic2Class))
