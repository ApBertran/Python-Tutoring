import cv2
import numpy as np

img = np.zeros((500,500,3), dtype=np.uint8)
clickList = list()
clickCount = 0
x1 = 0
y1 = 0
red = False
blue = False

def redraw_lines():
    global img, clickList
    pointX = 0
    pointY = 0
    pointColor = (0,0,0)
    
    for i in range(int(len(clickList) / 3)):
        pointX = clickList[i * 3]
        pointY = clickList[(i * 3) + 1]
        if clickList[(i * 3) + 2] == 'B':
            pointColor = (255,0,0)
        else:
            pointColor = (0,0,255)
        cv2.circle(img, (pointX,pointY), 5, pointColor, -1)

def redraw_background(x,y):
    global img
    if x > y:
        R = (y / x)
        G = (y / x)
        B = (y / x)
    else:
        R = (x / y)
        G = (x / y)
        B = (x / y)
        
    R = int(R * 255)
    G = int(G * 255)
    B = int(B * 255)
    
    cv2.rectangle(img, (0,0), (500,500), (R,G,B), -1)
        
def detect_click(event,x,y,flags,param):
    global img, clickCount, clickList, x1, y1, red, blue
    
    if event == cv2.EVENT_LBUTTONDOWN:
        redraw_background(x,y)
        redraw_lines()
        clickList.append(x)
        clickList.append(y)
        clickList.append("B")
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
        redraw_background(x,y)
        clickList.append(x)
        clickList.append(y)
        clickList.append("R")
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
        redraw_lines()
        #redraw_background(x,y)

def main():
    global img
    while True:
        cv2.imshow("image", img)
        cv2.waitKey(1)
        cv2.setMouseCallback("image", detect_click)

main()
