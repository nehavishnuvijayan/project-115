
'''
a=33
b=33
if b>a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")
'''
'''
import os
import shutil
source="D:/nv"
destination="D:/abc"
files=os.listdir(source)
print(files)
for i in files:
    name,ext=os.path.splitext(i)
    if ext==" ":
        continue
    if ext in ['.txt','.doc','.docx','.pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "document_files"
        path3 = destination + '/' + "document_files" + '/' + i
    if os.path.exists(path2):
        print("Moving")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("Moving")
        shutil.move(path1,path3)
'''
'''
import os
import shutil
source="D:/abc"
destination="C:\Users\User\OneDrive"
files=os.listdir(source)
print(files)
for i in files:
    name,ext=os.path.splitext(i)
    if ext==" ":
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Image_Files"
        path3 = destination + '/' + "Image_Files" + '/' + i
    if os.path.exists(path2):
        print("Moving")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("Moving")
        shutil.move(path1,path3)
'''