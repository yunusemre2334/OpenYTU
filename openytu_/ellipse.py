import cv2 

img_path = "images/barkan.jpg"

img = cv2.imread(img_path)


merkez = (150, 150)
eksenler = (150,50)


aci = 120
baslangic_acisi = 80
bitis_acisi = 350
renk = (0,0,255)
kalinlik = -1


cv2.ellipse(img, merkez, eksenler, aci,baslangic_acisi, bitis_acisi, renk,kalinlik)


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()