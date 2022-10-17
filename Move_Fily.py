
import os 
import shutil

from_dir = 'C:/users/SRI/Downloads/'
to_dir = 'Documents/'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for k in list_of_files:
 root,ext = os.path.splitext(k)
 print("root :",root)
 print("ext:",ext)
