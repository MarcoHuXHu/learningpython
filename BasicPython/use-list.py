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