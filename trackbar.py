import cv2 

cap = cv2.VideoCapture(0)


def nothing(x):
    pass

cv2.namedWindow("Trackbar", cv2.WINDOW_NORMAL)
cv2.createTrackbar("Threshold_low", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Threshold_high", "Trackbar", 0, 255, nothing)


while True:
    ret, frame = cap.read()

    if ret == False:
        break 

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    threshold_low_value = cv2.getTrackbarPos("Threshold_low", "Trackbar")
    threshold_high_value = cv2.getTrackbarPos("Threshold_high", "Trackbar")
    _, thresholded_frame = cv2.threshold(gray_frame, threshold_low_value, threshold_high_value, cv2.THRESH_BINARY)


    cv2.imshow("thresholded_frame", thresholded_frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break 

cap.release()
cv2.destroyAllWindows()














