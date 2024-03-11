import cv2 
import imutils

img_path = "images/siha.jpg"

img = cv2.imread(img_path)
resized_img = imutils.resize(img, width = 600)

cv2.circle(resized_img, (20,50), 6, (0,0,255), 2)
cv2.circle(resized_img, (120,150), 6, (0,255,0), -1)

# ctrl + k + c -> comment (yorum satırı yap)
# ctrl + k + u -> uncomment (yorum satırı olmaktan çıkar)

# cv2.imshow("img", img)
cv2.imshow("resized_img", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()