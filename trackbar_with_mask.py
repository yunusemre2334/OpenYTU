import cv2 
import numpy as np 


cap = cv2.VideoCapture(0)


def nothing(x):
    pass 

cv2.namedWindow("Trackbar", cv2.WINDOW_NORMAL)
cv2.createTrackbar("Lower H","Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower S","Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower V","Trackbar", 0, 255, nothing)

cv2.createTrackbar("Upper H","Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper S","Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper V","Trackbar", 0, 255, nothing)


while True:
    ret, frame = cap.read()

    if ret == False:
        break 

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower H","Trackbar")
    lower_s = cv2.getTrackbarPos("Lower S","Trackbar")
    lower_v = cv2.getTrackbarPos("Lower V","Trackbar")

    upper_h = cv2.getTrackbarPos("Upper H","Trackbar")
    upper_s = cv2.getTrackbarPos("Upper S","Trackbar")
    upper_v = cv2.getTrackbarPos("Upper V","Trackbar")

    lower = np.array([lower_h,lower_s,lower_v])
    upper = np.array([upper_h, upper_s,upper_v])

    mask = cv2.inRange(hsv_frame, lower, upper)
    color_detected_frame = cv2.bitwise_and(frame, frame, mask = mask)


    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("color_detected_frame", color_detected_frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break 

cap.release()
cv2.destroyAllWindows()
