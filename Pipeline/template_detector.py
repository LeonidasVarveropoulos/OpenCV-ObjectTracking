import cv2
import numpy as np
from matplotlib import pyplot as plt


cv2 = cv2.cv2

def detect_template(frame,template1):
    img = frame
    img2 = img.copy()
    template = cv2.imread(template1)

    # Scale template by area


    h,w = template.shape[:2]
    
    
    res = cv2.matchTemplate(img2,template,method = cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img2,top_left, bottom_right, 255, 2)

    cv2.imshow("test",img2)

    roi = (top_left[0],top_left[1],w,h)

    return roi

