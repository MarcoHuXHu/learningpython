#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable, Iterator, deque

# Iterable & Iterator

# 用iterator来生成杨辉三角
def triangle_iter(n):
    pre = [1]
    pro = [1, 1]
    i = 2
    yield pre
    if n == 1:
        return
    while i <= n:
        yield pro
        pre = pro
        # 注意：list的generator会先计算if成立时的值，因此这里必须把j==0 or j==i的情况写在if成立的情况，否则会index out of range
        pro = [1 if j==0 or j==i else pre[j]+pre[j-1] for j in range(i+1)]
        pro.append(1)
        i = i + 1


print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))  # True
print('Iterable? \'abc\':', isinstance('abc', Iterable))        # True
print('Iterable? 123:', isinstance(123, Iterable))              # False

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))  # False
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))  # True
print('Iterator? \'abc\':', isinstance('abc', Iterator))        # False
print('Iterator? 123:', isinstance(123, Iterator))              # False

it = triangle_iter(5)
while True:
    print(next(it))

