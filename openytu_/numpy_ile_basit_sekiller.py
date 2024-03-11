import cv2 
import numpy as np


# 0- 255 arasında 
# kanal -> 2  siyah - beyaz  0 - 255 
# kanal -> 3 kanal rgb, bgr, hsv ...     blue - > 0- 255,      green -> 0- 255  ,  red -> 0- 255

img_ones = np.ones((600, 400), np.uint8)
img_ones[30:100, 40: 80] = 110

cv2.line(img_ones, (30, 30), (200, 400), (255, 45, 0), 2)




cv2.imshow("img_ones", img_ones)



cv2.waitKey(0)
cv2.destroyAllWindows()