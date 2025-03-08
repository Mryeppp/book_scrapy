'''
序列化 把内存中的变量变成可存储或者可传输的过程就叫序列化
将序列化的内容写入磁盘或通过网络传输到别的机器上，可以实现程序状态的保存和共享。
反过来把序列化对象重新读取到内存中叫做反序列化
python中常用的序列化模块cPickle pickle。首选cPickle
'''
try:
    import cPickle as pickle # type: ignore
except ImportError:
    import pickle
    d = dict(url="index.html",title = "hello" ,content="123")
    f = open(r"C:\Users\MrYep\Desktop\Book-SocialMediaMiningPython\MyLearning\IO\a_c.py","wb")
    pickle.dump(d,f)
    f.close()
 
    f = open(r"C:\Users\MrYep\Desktop\Book-SocialMediaMiningPython\MyLearning\IO\a_c.py","rb")
    d = pickle.load(f)
    f.close()
    print(d)
    
