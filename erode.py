import cv2 
import imutils 
import numpy as np

img_path = "images/barkan.jpg"

img = cv2.imread(img_path)
img = imutils.resize(img, width=450)
kernel = np.ones((7,7), dtype = np.uint8)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

erode = cv2.erode(img_gray, kernel, iterations = 1)




cv2.imshow("img", img)
cv2.imshow("erode",erode)
cv2.waitKey(0)
cv2.destroyAllWindows()