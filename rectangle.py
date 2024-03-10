import cv2 

img_path = "images/barkan.jpg"

img = cv2.imread(img_path)

cv2.rectangle(img, (150, 80), (750, 450), (255,0,0), 3)


cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

