#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter传入一个返回True或False的函数，与一个Iterable对象，返回经过函数筛选为True的元素
# filter返回为iterator
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# 结果: [1, 5, 9, 15]

# 例1：筛选回文数

def is_palindrome(n):#0123456
    digits = str(n)
    length = len(digits)
    for i in range(length//2):
        if digits[i] != digits[length-i-1]:
            return False
    return True

print(list(filter(is_palindrome, range(100, 999))))

# 例2：筛选素数
# 方法1：直接筛选法

import math

def is_not_divisible(n):
    def func(x):
        return (x%n) > 0
    return func

def prime_number(n):
    primes = range(2, n+1)
    i = 2
    for i in range(2, int(math.sqrt(n))):
        primes = filter(is_not_divisible(i), primes)
    print(list(primes))

prime_number(100)

