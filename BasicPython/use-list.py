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


# slice
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