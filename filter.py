import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import random

def salt_pepper_noise(img):
    for n in range(512):
        i = round(random.random()*255)
        j = round(random.random()*255)
        k = round(random.random())
        if(k==1): k=255
        img[i,j] = k
    return img

img_raw = cv2.imread(os.getcwd()+"/in/lena.png",0)
img_noise = salt_pepper_noise(img_raw)
img_blur = cv2.blur(img_noise,(3,3))
img_median = cv2.medianBlur(img_noise,3)

cv2.imwrite(os.getcwd()+"/out/img_noise.png",img_noise)
cv2.imwrite(os.getcwd()+"/out/img_blur.png",img_blur)
cv2.imwrite(os.getcwd()+"/out/img_median.png",img_median)
cv2.imshow("img_noise",img_noise)
cv2.imshow("img_blur",img_blur)
cv2.imshow("img_median",img_median)
cv2.waitKey(0)


