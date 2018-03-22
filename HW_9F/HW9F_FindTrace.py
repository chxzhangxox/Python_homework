# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:06:21 2018

@author: chxzh
"""
#practice of template matching
#trace the movement of the hip
#utilize opencv2::VideoCapture, grab and retrieve function

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture('RyanRun.mp4')
temp = cv.imread('hip.png', 0)
w,h = temp.shape[::-1]

exclude1 = 870
exclude2 = 1080
i = 0
data = []

while(cap.isOpened()):
    if (cap.grab()):
        if i <= exclude1:
            i = i + 1
        elif i > exclude2:
            break
        else:
            ret, frame = cap.retrieve()
            h_img, w_img = frame.shape[0:2]
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            
            #if it is the first frame
            if i == exclude1 + 1:
                res = cv.matchTemplate(gray,temp,cv.TM_CCOEFF_NORMED)
                
                #get the location of one match
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                top_left = max_loc
                x_pos = top_left[0]
                y_pos = top_left[1]
                bottom_right = (x_pos + w, y_pos + h)
                data.append(top_left)
                
                #get adjacent area
                img_small = gray[max(0,y_pos - h): min(y_pos + 2*h, h_img), max(0,x_pos - w): min(x_pos + 2*w, w_img)]
            
            #if it is not the first frame
            else:
                #only search adjacent area
                img_small = gray[max(0,y_pos - h): min(y_pos + 2*h, h_img), max(0,x_pos - w): min(x_pos + 2*w, w_img)]
                res = cv.matchTemplate(img_small,temp, cv.TM_CCOEFF_NORMED)
                
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                top_left = (max(0,x_pos - w) + max_loc[0], max(0, y_pos - h) + max_loc[1])
                x_pos = top_left[0]
                y_pos = top_left[1]
                bottom_right = (x_pos + w, y_pos + h)
                data.append(top_left)
            
            #draw a rectangle around the match
            cv.rectangle(gray, top_left, bottom_right, (255,255,255), 2)
            img_small = gray[max(0,y_pos - h): min(y_pos + 2*h, h_img), max(0,x_pos - w): min(x_pos + 2*w, w_img)]
            cv.imshow('frame', gray)
            i = i + 1
            if cv.waitKey(1) == ord('q'):
                break

cap.release()
cv.destroyAllWindows()

#draw the graph of the movement of the hip   
x = [v[0] for v in data]
y = [v[1] for v in data]
plt.plot(x,y)
plt.gca().invert_yaxis()
plt.title('Hip Trace')
plt.xlabel('X Pixel')
plt.ylabel('Y Pixel')