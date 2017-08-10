def forloop(n) :
    for x in range(n) :
        print (x * x)

def dowhile(n) :
    x = 0
    while (x < n) :
        print (x * x)
        x = x + 1


if __name__ == '__main__':
    n = int(input())
    forloop(n)
    dowhile(n)
