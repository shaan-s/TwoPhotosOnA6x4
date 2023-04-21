def errExit():
    input()
    sys.exit()

import sys
from PIL import Image
from time import time

finalw=1800
finalh=1200
#6in x 4in at 300dpi
margin=100

if len(sys.argv) < 3:
    print("ERROR: You must drag + drop EXACTLY TWO files. Exiting now...")
    errExit()

imgs= [Image.open(sys.argv[1]),Image.open(sys.argv[2])]

print("Images imported... Working...")

for x in range(2):
    if imgs[x].width > imgs[x].height:
        imgs[x]=imgs[x].rotate(90,expand=1)
    imgs[x]=imgs[x].resize((int((finalh-margin)*(imgs[x].width/imgs[x].height)),(finalh-margin)))
    if imgs[x].width > finalw//2:
        imgs[x]=imgs[x].resize((finalw//2-margin,(int((finalw//2-margin)*(imgs[x].height/imgs[x].width)))))

im = Image.new("RGB", (finalw, finalh), (255,255,255))

im.paste(imgs[0],((finalw//2-imgs[0].width)//2,margin//2))
im.paste(imgs[1],(finalw//2+(finalw//2-imgs[1].width)//2,margin//2))

filename=f"{round(time())}.jpg"
im.save(filename, format=None)
print(f"{filename} created.")
im.show()
