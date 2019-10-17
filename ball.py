import cv2
from matplotlib import pyplot as plt
import numpy as np

cv2 = cv2.cv2

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernel = np.ones((35,35),np.uint8)
    kernel2 = np.ones((5,5),np.uint8)

    lower_yellow = np.array([20,80,80])
    upper_yellow = np.array([60,255,255])

    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel2)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    cool = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel2)

    norm_img = cv2.cvtColor(closing,cv2.COLOR_HSV2BGR)
    closing_gray = cv2.cvtColor(norm_img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(closing_gray,100,200)
    
    
    edge_img = cv2.imshow("Edges",edges)
    #cv2.imshow("Image", norm_img)
    cv2.imshow("original",frame)
    #cv2.imshow("gray",gray)
    #cv2.imshow("hsv",hsv)
    #cv2.imshow("mask",mask)
    #cv2.imshow("res",res)
    cv2.imshow("Final",closing)
    cv2.imshow("Final_gray",closing_gray)
    #cv2.imshow("cool",cool)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()