import os

print('Process (%s) start...' % os.getpid())

def run1():
    pid = os.fork()

    if pid == 0 :
        print('Child process, %s is son of %s' % (os.getpid(), os.getppid()))
    else :
        print('%s created %s' % (os.getpid(), pid))


run1() # 分为两个进程执行
# 0
# |
# 1
run1() # 两个进程都会执行这一句
# 0
# |\
# 1 2
# |
# 3