import os
import shutil

print(os.getcwd())
a = os.listdir("C:/Users/MrYep/Desktop/Book-SocialMediaMiningPython")
print(a)

# os.remove("C:/Users/MrYep/Desktop/Book-SocialMediaMiningPython/MyLearning/IO/a.txt")
# os.removedirs("C:/Users/MrYep/Desktop/Book-SocialMediaMiningPython/MyLearning/IO/a")
shutil.copyfile("MyLearning\\IO\\a.py","MyLearning\\IO\\a_ccc.py")
