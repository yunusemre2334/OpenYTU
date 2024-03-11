import cv2
import numpy as np 

cap = cv2.VideoCapture(0)



while True:
    ret, frame = cap.read()

    if ret == False:
        break 

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])

    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    blue_detected_frame = cv2.bitwise_and(frame, frame, mask = blue_mask)

    cv2.imshow("Orijinal Frame",frame)
    cv2.imshow("Mavi Renk Tespiti Arayüzü", blue_detected_frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break 
    
cap.release()
cv2.destroyAllWindows()
