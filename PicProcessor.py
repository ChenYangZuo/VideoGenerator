import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

def pic2text():
    img = cv2.imread(os.getcwd()+"/raw_data.png",0)
    img_file = open(os.getcwd()+'/raw_data.txt','w')
    for i in range(256):
        for j in range(256):
            img_file.write(str(img[i,j])+"\n")
    img_file.close()
    input("Success")

def text2pic():
    img_file = open(os.getcwd()+"/filter_data.txt",'r')
    img = np.zeros((256,256),dtype=np.uint8)
    for i in range(256):
        for j in range(256):
            if int(img_file.readline().strip('\n')) == 1:
                data = 255
            else:
                data = 0
            img[i,j] = data
    cv2.imshow("test",img)
    print("Success")
    cv2.imwrite(os.getcwd()+"/filter_data.png",img)
    cv2.waitKey(0)

def pic2histogram():
    hist = [0]*256
    img = cv2.imread(os.getcwd()+"/in/lena.png",0)
    for i in range(256):
        for j in range(256):
            hist[img[i,j]] = hist[img[i,j]] + 1
    print(hist)
    input("Success")
    plt.plot(hist)
    # plt.show()
    plt.savefig(os.getcwd()+"/out/lena_hist.png",bbox_inches='tight')

def text2histogram():
    hist_file = open(os.getcwd()+"/in/hist_tb.txt",'r')
    hist = [0]*256
    for i in range(256):
        hist[i] = int(hist_file.readline().strip('\n'),base=16)
    plt.plot(hist)
    # plt.show()
    plt.savefig(os.getcwd()+"/out/hist_tb.png",bbox_inches='tight')

while True:
    os.system("cls")
    print("Press [1] to convert picture to txt.")
    print("Press [2] to convert text to picture.")
    print("Press [3] to convert picture to histogram.")
    print("Press [4] to convert text to histogram.")

    choice = int(input("My choice is: "))
    if choice == 1:
        pic2text()
    elif choice == 2:
        text2pic()
    elif choice == 3:
        pic2histogram()
    elif choice == 4:
        text2histogram()
    else:
        input("ERROR CHOICE")