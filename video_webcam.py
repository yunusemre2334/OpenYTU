import cv2 
import imutils 

path = "videos/test.mp4"

cap = cv2.VideoCapture(path)


while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width= 800)
    if ret == False:
        break

    cv2.imshow("frame", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
