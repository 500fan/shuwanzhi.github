import os
import cv2

file_path = "E:\GitHub Desktop\GitHub\pictruebed\Avatar\\"
web_path = "https://cdn.jsdelivr.net/gh/anderson-ryen/pictruebed/Avatar"

def img_resize(image_path):
    image = cv2.imread(file_path+image_path)
    height, width = image.shape[0], image.shape[1]
    # 设置新的图片分辨率框架
    width_new = 580
    height_new = 580
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
       img = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
       img = cv2.resize(image, (int(width * height_new / height), height_new))
    if ".jpg" in image_path:
        cv2.imwrite(file_path+image_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    elif ".png" in image_path:
        cv2.imwrite(file_path+image_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

if __name__ == '__main__':
    filelist = os.listdir(file_path)
    with open('E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\Avatar.txt','w') as f:
        for file in filelist:
            img_resize(file)
            f.write(web_path+file+'\n')