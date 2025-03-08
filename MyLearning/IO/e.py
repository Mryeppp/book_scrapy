# 进程 多线程 协程 分布式进程
# os模块的fork方法 仅支持unix\linux
# multiprocessing模块 支持跨平台

# multiprocessing创建多进程
import os
from multiprocessing import Process
def run_proc(name) -> None:
    print ('child process %s (%s) running...' % (name, os.getpid()))
if __name__ == '__main__' :
    print ('father process %s ...' % os.getpid())
    for i in range(5):
        p = Process(target = run_proc, args = (str(i),))
        print('Process will start')
        p.start()
    p.join()
    print ('Process end.')
# 测试linux上传
