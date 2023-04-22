
import random
import shutil
import os
import cv2
a = 200



for i in range(a):
    shutil.copyfile("source/hoge.png","../hoge{}.png".format(i))
    img = cv2.imread("../hoge{}.png".format(i))
    re1 = cv2.resize(img, dsize=(700, 500))
    cv2.imshow('chikawa{}'.format(i), re1)
    a = random.randint(1,1500)
    b = random.randint(1,1500)
    cv2.moveWindow('chikawa{}'.format(i),a,b)
    cv2.waitKey(10) 
cv2.waitKey(0) 
