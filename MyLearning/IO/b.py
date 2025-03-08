with open(r"MyLearning\\IO\\text01.txt",'w') as f:
    f.write("1234")
    f.write("ada")
    f.write("d454")
    f.write("1dsa")
    f.write("112wed")
with open(r"MyLearning\IO\text01.txt",'r',encoding="utf-8") as f :
    for line in f.readlines():
        print(line.strip())
    
