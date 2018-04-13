import re


# s = 'ABC\\-001'
# s = r'ABC\-001'
# 使用Python的r前缀，就不用考虑转义的问题了

# match
match = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

print(match) # <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
re.match(r'^\d{2}\-\d{3,8}$', '010-12345') # None
re.match(r'^\d{3}\-\d{3,4}$', '010-12345') # None

# match & group
match = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
print(match.group(0)) # 010-12345
print(match.group(1)) # 010
print(match.group(2)) # 12345

# find all
str = '2015-6-1 08:10:30:000'
find = re.findall(r'(\d+):(\d+)', str)
print(find) # ('08', '10'), ('30', '000')]
result = re.finditer(r'(\d+):(\d+)', str)
print(next(result))
print(next(result))

# split
# 普通模式，不能识别多个空格
print('a b   c'.split(' '))                 # ['a', 'b', '', '', 'c']
# 利用re，识别多个空格
print(re.split(r'\s+', 'a b   c'))          # ['a', 'b', 'c']
# 利用re，识别多个空格，逗号，分号
print(re.split(r'[\s\,\;]+', 'a,b;; c  d')) # ['a', 'b', 'c', 'd']
print(re.split(r'[\,\;]+', 'a,b;; c ,; d')) # ['a', 'b', ' c ', ' d']

# matching model, greedy or not
# default: greedy, match as much as can
print(re.match(r'^(\d+)(0*)$', '102300').groups())  # ('102300', '')
# change to not greedy: with '?'
print(re.match(r'^(\d+?)(0*)$', '102300').groups()) # ('1023', '00')
