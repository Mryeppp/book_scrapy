# 线程池 pool
# 当子线程较多的时候 无法像e.py展示的方法一样一个一个手动创建
# multiprocessing 提供了 Pool类来代表线程池对象
# 下面的示例中线程池容量为3。但是以此添加了五个任务，但是线程池容量决定了每次最多运行三个进程
# 只有当一个任务结束了，新的任务才会进入线程池
# 而且新任务使用的进程依然是原来的进程，这一点看每个任务的pid即可
from multiprocessing import Pool
import os, time, random


def run_task(name):
    print("process (%s) [pid = (%s)] is runing ..." % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print("Task %s end" % (name))


if __name__ == "__main__":
    print("cur process %s" % (os.getpid()))
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print("waiting for all subprocesses done")
    p.close()
    p.join()
    print("all subprocesses done")
"""
cur process 1961
waiting for all subprocesses done
process (0) [pid = (1962)] is runing ...
process (1) [pid = (1963)] is runing ...
process (2) [pid = (1964)] is runing ...
Task 0 end
process (3) [pid = (1962)] is runing ...
Task 3 end
process (4) [pid = (1962)] is runing ...
Task 2 end
Task 1 end
Task 4 end
all subprocesses done
"""
