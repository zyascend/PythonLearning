# -*-coding:utf-8-*-
import os
import random
import time

from multiprocessing import Process, Queue
from multiprocessing import Pool


# def run_proc(name):
#     print('Run child process: %s (%s)' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('parent process: %s' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('child process start...')
#     p.start()
#     p.join()  # 子进程结束后继续运行
#     print('child process end...')


# 进程池
def long_time_task(name):
    print('task running %s (pid = %s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task (%s) runs [%0.2f] s...' % (name, (end - start)))


if __name__ == '__main__':
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all task done...')
    p.close()
    p.join()
    print('All subProcess done...')


# 进程间通信
def write(q):
    print('Process write: (%s)' % os.getpid())
    for v in ['A', 'B','C']:
        print('put [%s] in queue' % v)
        q.put(v)
        time.sleep(random.random())


def read(q):
    print('Process read: (%s)' % os.getpid())
    while True:
        v = q.get(True)
        print('get [%s] from queue' % v)


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=read, args=(q,))
    pr = Process(target=write, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pw.terminate()

