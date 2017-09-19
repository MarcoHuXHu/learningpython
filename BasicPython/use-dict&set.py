d = dict()
s = set()

d['a'] = 1
d['b'] = 2

s.add('x')
s.add('y')

print('a' in d)
print('x' in s)

print(d['a'])
print(d.get('a'))
# print(d['c'])     KeyError, using "get" will return None
print(d.get('c'))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
for k in d.keys():
    print('key:', k)

# iter each value:
for v in d.values():
    print('value:', v)

# iter both key and value:
for k, v in d.items():
    print('item:', k, v)