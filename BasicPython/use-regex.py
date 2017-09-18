import re


# s = 'ABC\\-001'
# s = r'ABC\-001'
# 使用Python的r前缀，就不用考虑转义的问题了

# find all

str = '2015-6-1 08:10:30:000'
result = re.findall(r'(\d+):(\d+)', str)
print(result) # ('08', '10'), ('30', '000')]
result = re.finditer(r'(\d+):(\d+)', str)
print(result)