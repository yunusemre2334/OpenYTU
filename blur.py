import cv2

img_path = "images/barkan.jpg"
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.blur(img_gray, (3,3))
gauss_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
median_blur = cv2.medianBlur(img_gray, 3)

_ ,th_mb = cv2.threshold(median_blur, 140, 250, cv2.THRESH_BINARY)
_ ,th_g = cv2.threshold(gauss_blur, 140, 250, cv2.THRESH_BINARY)
_ ,th_b = cv2.threshold(blur, 140, 250, cv2.THRESH_BINARY)



cv2.imshow("img", img)
# cv2.imshow("blur", blur)
# cv2.imshow("gauss_blur", gauss_blur)
# cv2.imshow("median_blur", median_blur)
cv2.imshow("th_mb", th_mb)
cv2.imshow("th_b", th_b)
cv2.imshow("th_g", th_g)


cv2.waitKey(0)
cv2.destroyAllWindows()