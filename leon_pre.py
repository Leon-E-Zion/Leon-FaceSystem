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





# 获取模型
def get_model():
    retinaface = Retinaface()
    return retinaface

# 支持送入图片 - 之后可扩展为支持送入视频
def get_role(net,path):
    image = cv2.imread(path)
    image   = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    r_image,name =net.detect_image(image)
    r_image = cv2.cvtColor(r_image,cv2.COLOR_RGB2BGR)
    cv2.imwrite('a.jpg',r_image)
    return {'output_img':r_image,'output_name':name}



if __name__ == "__main__":
    retinaface = Retinaface()
    img = r'D:\Leon-Coding\Leon_TestData\hg-1.png'
    image = cv2.imread(img)
    image   = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    r_image = retinaface.detect_image(image)
    r_image = cv2.cvtColor(r_image,cv2.COLOR_RGB2BGR)
    cv2.imwrite('a.jpg',r_image)

