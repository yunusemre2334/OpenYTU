import cv2

img_path = "images/elma.jpg"

img = cv2.imread(img_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.blur(img_gray, (3,3))

_, th = cv2.threshold(img_blur, 200, 230, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    perimeter = cv2.arcLength(cnt, True)
    area = cv2.contourArea(cnt)
    if area < 15000:
        epsilon = 0.02 * perimeter
        approx_polygon = cv2.approxPolyDP(cnt, epsilon, True)
        print("çevre: {}  çokgen {} kenarlıdır.".format(int(perimeter), len(approx_polygon)))
        cv2.drawContours(img, [cnt], -1, (0,255,0), 2)


cv2.imshow("img", img)
cv2.imshow("th", th)

cv2.waitKey(0)
cv2.destroyAllWindows()