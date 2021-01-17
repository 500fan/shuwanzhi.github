# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:20:20 2020

@author: Anderson Ryen
"""

import os


file_path = "E:\GitHub Desktop\GitHub\picturebad-two\sexy-two\\"
web_path = "https://cdn.jsdelivr.net/gh/anderson-ryen/pictruebed-two/sexy-two/"

if __name__ == '__main__':
    filelist = os.listdir(file_path)
    with open(r'E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\sexy-two.txt','w') as f:
        for file in filelist:
            f.write(web_path+file+'\n')