# -*-coding:utf-8-*-
# datetime
from collections import namedtuple
from datetime import datetime

now = datetime.now()
print(now)
dt = datetime(2017, 4, 20, 14, 28)
print(dt)
# 把datetime转换为timestamp
ts = dt.timestamp()
print(ts)
# 翻转
print(datetime.fromtimestamp(ts))
# str转换为datetime
timeString = '2015-6-1 18:19:59'
cday = datetime.strptime(timeString, '%Y-%m-%d %H:%M:%S')
print(cday)
# 反转
print(now.strftime('%a, %b %d %H:%M'))

# collections
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 5)
print('x = %s, y = %s' % (p.x, p.y))

