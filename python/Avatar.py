import os
import cv2

file_path = "E:\GitHub Desktop\GitHub\pictruebed\Avatar\\"
web_path = "https://cdn.jsdelivr.net/gh/anderson-ryen/pictruebed/Avatar/"



if __name__ == '__main__':
    filelist = os.listdir(file_path)
    with open(r'E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\Avatar.txt','w') as f:
        for file in filelist:
            img_resize(file)

            f.write(web_path+file+'\n')