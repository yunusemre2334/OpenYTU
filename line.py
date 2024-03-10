import cv2 
import numpy as np


# kanal -> 3 kanal rgb, bgr, hsv ...     blue - > 0- 255,      green -> 0- 255  ,  red -> 0- 255

img_path = "images/barkan.jpg"

img = cv2.imread(img_path)
cv2.line(img, (30, 30), (500, 400), (0, 250,0 ), 8)
cv2.line(img, (10, 30), (340, 200), (250, 0,0 ), 8)
cv2.line(img, (20, 30), (500, 100), (0, 0,250 ), 8)

cv2.imshow("img", img)



cv2.waitKey(0)
cv2.destroyAllWindows()