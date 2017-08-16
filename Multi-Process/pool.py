from multiprocessing import Pool
import os, time

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(name)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)             # 设定最多同时跑的进程数
    for i in range(8):      # 先执行前面4个进程，而后的须等待之前执行完了才能继续
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()               # close之后就不能在进程池中开新的进程
    p.join()                # 必须要close之后才可以join
    print('All subprocesses done.')