import cv2 

img_path = "images/barkan.jpg"
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(img_gray, 150, 230, cv2.THRESH_BINARY)
_, th_inv = cv2.threshold(img_gray, 150, 230, cv2.THRESH_BINARY_INV)


cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)
cv2.imshow("th", th)
cv2.imshow("th_inv", th_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()