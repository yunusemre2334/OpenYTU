import cv2 
import easyocr
import numpy as np

image_path = "images/licence_plate.jpg"
img = cv2.imread(image_path)

reader = easyocr.Reader(['en'], gpu = False)
text_ = reader.readtext(img)

threshold = 0.60

for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t
    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 2)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 1, cv2.LINE_AA)


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
