def gen_one():
    subgen = range(10)
    yield from subgen

def gen_two():
    subgen = range(10)
    for item in subgen:
        yield item

# print(list(gen_one()))
# print(list(gen_two()))

def gen():
    yield from subgen()

def subgen():
    while True:
        x = yield
        yield x+1

def main():
    g = gen()
    next(g)                # 驱动生成器g开始执行到第一个 yield
    retval = g.send(1)     # 看似向生成器 gen() 发送数据
    print(retval)          # 返回2
    g.throw(StopIteration) # 看似向gen()抛入异常

main()