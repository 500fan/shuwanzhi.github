# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:20:54 2021

@author: Anderson Ryen
"""

import os
#预览地址
view_path = "https://www.opbe.top/php-api/sexy.php"
#文件的绝对路径
file_path_1 = "E:\GitHub Desktop\GitHub\sexy-20-12-12\sexy\\"
file_path_2 = "E:\GitHub Desktop\GitHub\sexy-21-1-17\sexy\\"
file_path_3 = "E:\GitHub Desktop\GitHub\sexy-21-2-13\sexy\\"
file_path_4 = "E:\GitHub Desktop\GitHub\sexy-21-3-3\sexy\\"
#CDN前缀
web_path = "https://cdn.jsdelivr.net/gh/"
#GITHUB账户名
user_path = "anderson-ryen"
#仓库名
warehouse_path_1 = "sexy-20-12-12"
warehouse_path_2 = "sexy-21-1-17"
warehouse_path_3 = "sexy-21-2-13"
warehouse_path_4 = "sexy-21-3-3"
#仓库内文件夹
img_path = "sexy"
#合并path
api_path_1 = os.path.join( web_path + user_path + "/" + warehouse_path_1 + "/" + img_path + "/")
api_path_2 = os.path.join( web_path + user_path + "/" + warehouse_path_2 + "/" + img_path + "/")
api_path_3 = os.path.join( web_path + user_path + "/" + warehouse_path_3 + "/" + img_path + "/")
api_path_4 = os.path.join( web_path + user_path + "/" + warehouse_path_4 + "/" + img_path + "/")

print("")
print("效果预览: " + view_path)
print("=" *50)
print("sexy-已完成")
print("=" *50)
print("")

if __name__ == '__main__':
    filelist = os.listdir(file_path_1)
    with open(r"E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\sexy.txt",'w') as f:
        for file in filelist:
            f.write(api_path_1+file+'\n')

    filelist = os.listdir(file_path_2)
    with open(r"E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\sexy.txt",'a') as f:
        for file in filelist:
            f.write(api_path_2+file+'\n')

    filelist = os.listdir(file_path_3)
    with open(r"E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\sexy.txt",'a') as f:
        for file in filelist:
            f.write(api_path_3+file+'\n')

    filelist = os.listdir(file_path_4)
    with open(r"E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\sexy.txt", 'a') as f:
        for file in filelist:
            f.write(api_path_4 + file + '\n')