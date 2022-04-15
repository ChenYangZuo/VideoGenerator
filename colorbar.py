import cv2
import numpy as np
import os

img = np.zeros((256,256),np.uint8)

for i in range(8):
    img[:,32*i:32*(i+1)] = 30*i

if os.path.exists(os.getcwd()+"/img") == False:
    os.mkdir(os.getcwd()+"/img")

for i in range(256):
    new_img = np.roll(img,i) # 右移40个像素
    np.savetxt(os.getcwd()+f'/img/{i}.txt',new_img,fmt='%d')
