import os
import shutil
source = "C:/Users/Dell/Downloads"
destination = "C:/Users/Dell/Downloads"
list = os.listdir(source)
print(list)
for i in list:
    name,ext = os.path.splitext(i)
    print(name)
    print(ext)
    if ext == "":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "document_Files"
        path3 = destination + '/' + "document_Files" + '/' + i     
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)  
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)