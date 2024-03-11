import cv2 

img_path = "images/siha.jpg"

img = cv2.imread(img_path)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, "bu bir sihadir",(380,120), font, 2.5, (0,120,150), 5, cv2.LINE_AA)


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

