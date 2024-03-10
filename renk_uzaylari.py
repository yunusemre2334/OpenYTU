import cv2 

img_path = "images/barkan.jpg"

img = cv2.imread(img_path)
#  b - >  blue   g - > green  r - > red (45,34,35)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# siyah   beyaz  0-255
# print(img.shape)
# print(img_gray.shape)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# h  -> hue     s -> saturation    v -> value
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#rgb   =  r - > red  g - > green b - >  blue  (45,34,35)

cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)
cv2.imshow("img_hsv", img_hsv)
cv2.imshow("img_rgb", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()