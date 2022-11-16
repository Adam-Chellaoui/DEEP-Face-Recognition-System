import shutil

root = "/Users/mcol/Documents/INSA/ML/DEEP-Face-Recognition-System/My_data/wow"

# import required module
import os
 
# assign directory
directory = root
 
# iterate over files in
# that directory
i = 0
for filename in os.scandir(directory):
    if filename.is_dir():
        for pictures in os.scandir(filename.path):
            print(pictures.path)
            shutil.move(pictures.path, "/Users/mcol/Documents/INSA/ML/DEEP-Face-Recognition-System/My_data/wow/ALL/"+str(i))
            i+=1