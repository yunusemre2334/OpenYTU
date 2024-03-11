import cv2 

img_path = "images/araba.jpg"


img = cv2.imread(img_path)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()