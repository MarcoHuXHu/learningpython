def gen_a():
    subgen = range(10)
    yield subgen

def gen_b():
    subgen = range(10)
    yield from subgen

def gen_c():
    subgen = range(10)
    for i in subgen:
        yield i

# 例1：利用yield和yield from从生成器读取数据
# 可以看到gen_b和gen_c是等价的
def example1():
    print(list(gen_a())) # [range(0, 10)]
    print(list(gen_b())) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(gen_c())) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# 例2：利用yield from语句向生成器（协程）传送数据
def example2():
    w = writer()
    # wrap = writer_wrapper1(w)
    wrap = writer_wrapper2(w)

    wrap.send(None)  # 生成器准备好接收数据
    for i in range(4):
        wrap.send(i)

# 生成器writer，接收传送给它的数据并输出
def writer():
    # 读取send传进的数据，并模拟写进套接字或文件
    while True:
        w = (yield)    # w接收send传进的数据
        print('>> ', w)

# 问题：包装器函数如何传送数据给writer函数，使得传递给包装器的数据都能够显示地传递给writer函数
# 利用普通的yield
def writer_wrapper1(coro):
    coro.send(None)
    try:
        while True:
            x = (yield)  # 接收传给wrap层的数据
            coro.send(x) # 将数据发送给生成器（协程）
    except StopIteration:
        return

# 利用yield from
def writer_wrapper2(coro):
    yield from coro      # 是不是很简单

example2()