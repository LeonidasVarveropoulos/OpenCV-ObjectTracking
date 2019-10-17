import cv2
from matplotlib import pyplot as plt
import numpy as np
from color_filter import color_filter

cv2 = cv2.cv2

while True:
    frame = cv2.imread("template.jpg")
    
    
    cv2.imshow("Final_img",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

bbox = cv2.selectROI("final_img",frame)
print(bbox)

template = frame[bbox[1]:bbox[1] + bbox[3],bbox[0]:bbox[0] + bbox[2]]

while True:
    cv2.imshow("template",template)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("contour_template.jpg", template)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break