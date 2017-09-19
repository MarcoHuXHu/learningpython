def init(x, y) :
    res = []
    for i in range(x) :
        row = []
        for j in range(y) :
            row.append(i*10 + j)
        res.append(row)
    return res

if __name__ == '__main__':
    print(init(3,4))


# Slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-3::2] =', L[-3::2])
print('L[-3::-2] =', L[-3::-2])
'''
L[0:3] = ['Michael', 'Sarah', 'Tracy']
L[:3] = ['Michael', 'Sarah', 'Tracy']
L[1:3] = ['Sarah', 'Tracy']
L[-3::2] = ['Tracy', 'Jack']
L[-3::-2] = ['Tracy', 'Michael']
'''
R = list(range(100))
print('R[:10] =', R[:10])
# '-x:'表示倒数
print('R[-10:-5:2] =', R[-10:-5:2])
print('R[10:20] =', R[10:20])
# 第二个':'表示间距
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])
'''
R[:10] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
R[-10:-5:2] = [90, 92, 94]
R[10:20] = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
R[:10:2] = [0, 2, 4, 6, 8]
R[::5] = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
'''

# List Generator
print(list(range(1, 11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 注意是10不是11
print([x * x for x in range(1, 11)]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1, 11) if x % 2 == 0]) # [4, 16, 36, 64, 100]
print([m + n for m in 'ABC' for n in 'XYZ']) # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()]) # ['y=B', 'z=C', 'x=A']
L = ['Hello', 'World', 5, 'IBM', 'Apple']
print([s.lower() for s in L if isinstance(s, str)]) # ['hello', 'world', 'ibm', 'apple']