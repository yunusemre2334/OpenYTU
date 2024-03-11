import cv2 
import numpy as np 
import imutils

def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    #ROI (Region of Interest -> İlgi Alanı)
    height, width = frame.shape[:2]
    roi_vertices = [(0, height), (width/2, height/2), (width, height)]
    mask = np.zeros_like(gray)
    cv2.fillPoly(mask, np.int32([roi_vertices]), 255)
    masked_img = cv2.bitwise_and(edges, mask)

    lines = cv2.HoughLinesP(masked_img, 1, np.pi/180, threshold = 50, minLineLength=50, maxLineGap=50)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1,y1), (x2,y2), (0,255,0), 5)

    
    return frame, edges, mask, masked_img

cap = cv2.VideoCapture("videos/video2.mp4")


while True:
    ret, frame = cap.read()

    if ret == False:
        break

    frame, edges, mask, masked_img = process_frame(frame)

    frame = imutils.resize(frame, width=600)
    edges = imutils.resize(edges, width=600)
    mask = imutils.resize(mask, width=600)
    masked_img = imutils.resize(masked_img, width=600)

    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)
    cv2.imshow("mask", mask)
    cv2.imshow("masked_img", masked_img)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break 

cap.release()
cv2.destroyAllWindows()