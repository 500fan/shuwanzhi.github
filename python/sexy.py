# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:20:20 2020

@author: Anderson Ryen
"""

import os
import cv2

file_path = "E:\GitHub Desktop\GitHub\pictruebed\sexy\\"
web_path = "https://cdn.jsdelivr.net/gh/anderson-ryen/pictruebed/sexy/"


if __name__ == '__main__':
    filelist = os.listdir(file_path)
    with open(r'E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\sexy.txt','w') as f:
        for file in filelist:
            f.write(web_path+file+'\n')