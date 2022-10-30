import cv2
import numpy as np

img = np.zeros((500,500,3), dtype=np.uint8)

def detect_click(event,x,y,flags,param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 5, (255,255,255), -1)

def main():
    global img
    while True:
        cv2.imshow("image", img)
        cv2.waitKey(1)
        cv2.setMouseCallback("image", detect_click)

main()
