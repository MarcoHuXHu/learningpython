# 比较list与deque在stack与queue的区别
# stack：append + pop，两者耗时差距不大
# queue：insert(0)/appendleft + pop，两者差异巨大

import time
from collections import deque

a = list(range(100000))

b = deque(range(100000))

start = time.clock()

for i in range(100000):
    a.insert(0, i)
    a.pop()


end = time.clock()
print("list: ", end-start) # 5.818

start = time.clock()

for i in range(100000):
    b.appendleft(i)
    b.pop()

end = time.clock()
print("deque: ", end-start) # 0.022