# 进程 多线程 协程 分布式进程
# os模块的fork方法 仅支持unix\linux
# multiprocessing模块 支持跨平台


# fork 方法是调用一次返回两次，fork方法的原理是从当前进程中复制一个一模一样的进程
# 所以会在父子进程都产生返回值，子进程返回0 ， 父进程返回子进程的ID

# import os模块的fork方法
'''
import os
if __name__ =='__main__' :
    print('cur process (%s) start' %(os.getpid()))
    pid = os.fork()
    print(pid)
    if pid < 0 :
        print("error fork")
    elif pid == 0:
        print('i am a child process (%s) and my parent process is (%s)' %(os.getpid(),os.getppid()))
        # getppid()返回当前进程的父进程ID,getpid()返回当前进程ID
    else:
        print('I (%s) create a process (%s)' %(os.getpid() , pid))
'''
# multiprocessing创建多进程
import os
from multiprocessing import Process
def run_proc(name) -> None:
    print ('child process %s (%s) running...' % (name, os.getpid()))
if __name__ == '__main__' :
    print ('father process %s ...' % os.getpid())
    for i in range(5):
        p = Process(target = run_proc, args = (str(i),))# 调用了子进程p = run_proc(str(i))
        print('Process will start')
        p.start() # 启动进程
    p.join() # 进程间的通信
    print ('Process end.')

