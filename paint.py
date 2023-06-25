import cv2
import numpy as np
import os
import HandModule as hm
purple=(255 ,0,255)
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
black = (0, 0, 0)

Path = 'C:/Users/Mehrdad/PycharmProjects/Files and codes/virtual paint/toolbar'
toolbars = os.listdir(Path)
toolbar = []

for toolpath in toolbars:
    image = cv2.imread(Path + "/" + toolpath)
    toolbar.append(image)  # save all images in toolbar with append

menu = toolbar[0]
menu = cv2.resize(menu, (1280, 125))
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
color = blue
detector = hm.Detector(detectionCon=0.7, maxHands=1)

#=========================================================================
#def coord(event  , x, y, flags , param):
    #if event == cv2.EVENT_LBUTTONDOWN:
        #print(f'x = {int(x)}  , y= {int(y)}')

#cv2.namedWindow("Paint")
#cv2.setMouseCallback("Paint", coord)
#==========================================================================
x0   , y0 = 0 , 0
blank = np . zeros( (720,1280,3), np.uint8)
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame[0:125, 0:1280] = menu
    frame = detector.findHands(frame)
    landmarklist = detector.Position(frame, draw=False)
    if len(landmarklist) != 0:
        x1, y1 = landmarklist[8][1], landmarklist[8][2]
        x2, y2 = landmarklist[12][1], landmarklist[12][2]
        fin_pos = detector.fing_up()
        #print(fin_pos)
        if fin_pos[0] and fin_pos[1]:
            #print("selection")

            if y1<125:
                 if 250<x1<450:
                     color = blue
                     menu  = toolbar[0]
                 if 550<x1<750:
                     color = purple
                     menu = toolbar[1]
                 if  800<x1<950:
                     color = green
                     menu = toolbar[2]
                 if 1050<x1<1200:
                     color = black
                     menu = toolbar[3]

            cv2.rectangle(frame ,( x1 , y1 -20) ,( x2 , y2+20), color,-1 )
        if fin_pos[0] and fin_pos[1] == False:
            print("drawing")
            if x0 == 0  and y0 ==0:
                x0   ,y0 = x1 , y1
            cv2.circle(frame, (x1 ,y1), 12 , color, -1)
            cv2.line(frame , (x0 , y0) , (x1 , y1) , color , 12)
            cv2.line(blank , (x0, y0), (x1, y1), color, 12)
            x0  ,y0 = x1 , y1

    Gray = cv2.cvtColor(blank  , cv2.COLOR_BGR2GRAY)
    _ , Inv  = cv2.threshold(Gray , 0 , 255 , cv2.THRESH_BINARY_INV)

    cv2.imshow("inverse", Inv)
    cv2.imshow("blank", blank)
    cv2.imshow("Paint", frame)
    cv2.waitKey(1)




