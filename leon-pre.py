# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:37:54 2022

@author: leonz
"""

#----------------------------------------------------#
#   对视频中的predict.py进行了修改，
#   将单张图片预测、摄像头检测和FPS测试功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
#----------------------------------------------------#
import time

import cv2
import numpy as np

from retinaface import Retinaface

if __name__ == "__main__":
    retinaface = Retinaface()
    img = r'D:\Leon-Coding\Leon_TestData\hg-1.png'
    image = cv2.imread(img)
    image   = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    r_image = retinaface.detect_image(image)
    r_image = cv2.cvtColor(r_image,cv2.COLOR_RGB2BGR)
    cv2.imwrite('a.jpg',r_image)

