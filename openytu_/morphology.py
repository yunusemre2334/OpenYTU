import cv2 
import numpy as np 
import imutils

img_path = "images/elma.jpg"

img = cv2.imread(img_path)
img = imutils.resize(img, width=600)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((3,3), dtype = np.uint8)


acilis = cv2.morphologyEx(img_gray, cv2.MORPH_OPEN, kernel)
kapanis = cv2.morphologyEx(img_gray, cv2.MORPH_CLOSE, kernel)
degrade = cv2.morphologyEx(img_gray, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img_gray, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img_gray, cv2.MORPH_BLACKHAT, kernel)



cv2.imshow("img", img)
cv2.imshow("acilis", acilis)
cv2.imshow("kapanis", kapanis)
cv2.imshow("degrade", degrade)
cv2.imshow("tophat", tophat)
cv2.imshow("blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()