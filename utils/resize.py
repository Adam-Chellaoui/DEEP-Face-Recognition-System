from PIL import Image
import os

basewidth = 32
i = 1

for filename in os.scandir("My_data/Faces"):
    img = Image.open(filename.path)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
    img.save(str(i) + '.jpg')
    i+=1