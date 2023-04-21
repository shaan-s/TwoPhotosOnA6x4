def errExit():
    input()
    sys.exit()

import sys
from PIL import Image
from time import time

try:
    file1 = sys.argv[1]
except:
    print("ERROR: You must drag + drop the files. Exiting now...")
    errExit()
try:
    file2 = sys.argv[2]
except:
    print("ERROR: You must drag + drop EXACTLY TWO files. Exiting now...")
    errExit()
print("Images imported... Working...")

imgs= [Image.open(file1),Image.open(file2)]

for x in range(2):
    if imgs[x].width > imgs[x].height:
        imgs[x]=imgs[x].rotate(90,expand=1)
    imgs[x]=imgs[x].resize((int(2200*(imgs[x].width/imgs[x].height)),2200))
    if imgs[x].width > 1800:
        imgs[x]=imgs[x].resize((1800,(int(1800*(imgs[x].height/imgs[x].width)))))

im = Image.new("RGB", (3600, 2400), (255,255,255)) #6in x 4in at 600dpi

im.paste(imgs[0],((1800-imgs[0].width)//2,100))
im.paste(imgs[1],(1800+(1800-imgs[1].width)//2,100))

filename=f"{round(time())}.jpg"
im.save(filename, format=None, )
print(f"{filename} created.")
im.show()
