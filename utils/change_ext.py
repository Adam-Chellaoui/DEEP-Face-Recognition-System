from pathlib import Path
import shutil
import os

p = Path('/Users/mcol/Documents/INSA/ML/DEEP-Face-Recognition-System/My_data/cifar-test')
end = '/Users/mcol/Documents/INSA/ML/DEEP-Face-Recognition-System/My_data/cifar-test-jpg/'

i = 0

for filename in os.scandir(p):
    shutil.move(filename.path, end + str(i) + '.jpg')
    i+=1