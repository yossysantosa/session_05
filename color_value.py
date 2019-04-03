## Yossy Santosa
## image trump.jpg is subjected to www.slate.com

import cv2
import numpy as np
import csv

# global variables
imv_rgb = list()
imv_cmyk = list()
error = list()

# image processing function
def img_process(im, j, i):
    pixel = im[i, j]
    r = pixel[2]
    g = pixel[1]
    b = pixel[0]

    r1 = 1-r/255
    g1 = 1-g/255
    b1 = 1-b/255

    if (r1==1) and (g1==1) and (b1==1):
        imv_rgb.append([r,g,b])
        imv_cmyk.append([0,0,0,100])
        error.append([i,j])
        return
    else:
        k = min(r1, g1, b1)
        c = (r1-k)*100/(1-k)
        m = (g1-k)*100/(1-k)
        y = (b1-k)*100/(1-k)
        k = k*100

        c = int(round(c))
        m = int(round(m))
        y = int(round(y))
        k = int(round(k))

        imv_rgb.append([r,g,b])
        imv_cmyk.append([c,m,y,k])

## input picture
im=cv2.imread("trump.jpg",cv2.IMREAD_COLOR)
height, width = im.shape[:2]
# w, h = 238, 274
im = cv2.resize(im, (width, height), interpolation = cv2.INTER_CUBIC)

## show picture
#cv2.imshow("Images",im)

## image processing
for a in range(0,width):
    for b in range(0,height):
        img_process(im, a, b)

## export RGB image value to CSV
with open("rgb.csv", "w") as f1:
    wr = csv.writer(f1, delimiter=",")
    wr.writerow(imv_rgb)

with open("cmyk.csv", "w") as f2:
    wr = csv.writer(f2, delimiter=",")
    wr.writerow(imv_cmyk)

print("success")
