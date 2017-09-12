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



from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)




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
