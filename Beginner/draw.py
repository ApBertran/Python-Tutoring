import cv2
import numpy as np

img = np.zeros((500,500,3), dtype=np.uint8)
clickCount = 0
x1 = 0
y1 = 0
red = False
blue = False

def detect_click(event,x,y,flags,param):
    global img, clickCount, x1, y1, red, blue
    
    if event == cv2.EVENT_LBUTTONDOWN:
        clickCount += 1
        blue = True
        if clickCount != 2:
            x1 = x
            y1 = y
        else:
            clickCount = 0
            if blue and red:
                cv2.line(img, (x1,y1), (x,y), (255,0,255), 5)
            else:
                cv2.line(img, (x1,y1), (x,y), (255,0,0), 5)
            blue = False
            red = False
        cv2.circle(img, (x,y), 5, (255,0,0), -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        clickCount += 1
        red = True
        if clickCount != 2:
            x1 = x
            y1 = y
        else:
            clickCount = 0
            if blue and red:
                cv2.line(img, (x1,y1), (x,y), (255,0,255), 5)
            else:
                cv2.line(img, (x1,y1), (x,y), (0,0,255), 5)
            red = False
            blue = False
        cv2.circle(img, (x,y), 5, (0,0,255), -1)

def main():
    global img
    while True:
        cv2.imshow("image", img)
        cv2.waitKey(1)
        cv2.setMouseCallback("image", detect_click)

main()
