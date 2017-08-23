from multiprocessing import Process, Queue
import os, time

def write_to_queue(q):
    print('Process to write: %s' % os.getpid())
    for value in range(1, 10):
        # print('Put %s to queue...' % value)
        print('Write to queue', value)
        q.put(value)
        time.sleep(1)


def read_from_queue(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Read from queue', value)
        time.sleep(2)


if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    p1 = Process(target=write_to_queue, args=(q,))
    p2 = Process(target=read_from_queue, args=(q,))
    p1.start();
    p2.start();
    p1.join();
    p2.terminate();