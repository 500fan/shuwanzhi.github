import os
import cv2

file_path = "E:\GitHub Desktop\GitHub\picturebad\Resolution\\"
web_path = "https://cdn.jsdelivr.net/gh/anderson-ryen/pictruebed/Resolution/"




if __name__ == '__main__':
    filelist = os.listdir(file_path)
    with open(r'E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\Resolution.txt','w') as f:
        for file in filelist:

            f.write(web_path+file+'\n')