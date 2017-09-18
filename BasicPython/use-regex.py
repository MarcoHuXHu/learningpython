import re


# s = 'ABC\\-001'
# s = r'ABC\-001'
# 使用Python的r前缀，就不用考虑转义的问题了

# match

match = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
re.match(r'^\d{2}\-\d{3,8}$', '010-12345') # None
re.match(r'^\d{3}\-\d{3,4}$', '010-12345') # None
print(match)

# find all

str = '2015-6-1 08:10:30:000'
find = re.findall(r'(\d+):(\d+)', str)
print(find) # ('08', '10'), ('30', '000')]
result = re.finditer(r'(\d+):(\d+)', str)
print(next(result))
print(next(result))
