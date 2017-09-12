# namedtuple：可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)

isinstance(p, Point) # True
isinstance(p, tuple) # True

# json to namedtuple json转化为类似于model, 例子可见最后
import json
def _json_object_hook(d): return namedtuple('JSON', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


# deque：高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
print(q.popleft())
print(q)



# defaultdict：使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])



# OrderedDict：使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：

from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od['z'] = 4; od['y'] = 5; od['x'] = 'X'
print(od)

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # 普通都dict是无序的
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        # super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False) # 默认last=True，即pop最后一个
            print('remove:', last)
        if containsKey:
            # del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

FIFO = LastUpdatedOrderedDict(3)
FIFO['1'] = 'A'; FIFO['2'] = 'B'; FIFO['3'] = 'C';
print(FIFO)
FIFO['3'] = 'D';
print(FIFO)
FIFO['4'] = 'F';
print(FIFO)



# Counter：实际上也是dict的一个子类

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)



# json to namedtuple

json_object = {
   "externalRef":"1547",
   "clientCode":"14INVIBITEST",
   "marketType":"E",
   "accountNumber":"0I",
   "totalFinancingAmount":1.00,
   "payeeAccount": "000001",
   "financingInstruments":[
        {
          "custCode":"150ONIN101",
          "documentNo":"IBIINVD0I1",
          "indicativeAmount":1.00
        },
        {
          "custCode":"150ONIN101",
          "documentNo":"IBIINVD0I3",
          "indicativeAmount":1.00
        }
    ]
}


activities = json2obj(json.dumps(json_object))

print(activities)
