import cv2
import numpy as np 

img_path = "images/elma.jpg"

img = cv2.imread(img_path)


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)

edges = cv2.Canny(img_blur, 50, 150)



cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)
cv2.imshow("img_blur", img_blur)
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

