import cv2 

img_path = "images/araba.jpg"


img = cv2.imread(img_path)
#print(img.shape)

roi_img = img[20:150, 30:260]

cv2.imshow("img", img)
cv2.imshow("roi_img", roi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()