import cv2
import numpy as np 

img_path = "images/elma.jpg"

img = cv2.imread(img_path)


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (5,5), 0)

edges = cv2.Canny(img_blur, 50, 180)

kernel = np.ones((5,5), np.uint8)

dilated_img = cv2.dilate(edges, kernel, iterations = 1)


cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)
cv2.imshow("img_blur", img_blur)
cv2.imshow("dilated_img", dilated_img)
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

