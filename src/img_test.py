# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:28:19 2020

@author: Grace Wu
"""
import cv2
import numpy as np
import imutils

#parameters
imagepath = 'C:/Users/Grace Wu/m19/src/img/target1.jpg'
resizedw = 500
resizedh = 375
slowrad = 80
stoprad = 100

def findcircle(imagepath):
    #import image
    image = cv2.imread(imagepath)
    #make picture smaller
    resized = imutils.resize(image, width=resizedw)
    final = resized.copy()
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    #make colour filter
    g = [np.array([40,40,90]), np.array([100,100,380])]
    r = [np.array([120,50,80]), np.array([300,130,160])]
    b = [np.array([80,80,105]), np.array([150,150,380])]
    colours = [b,r,g]
    for i in colours:
        hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,i[0],i[1])
        img = cv2.bitwise_and(resized, resized, mask=mask)
        cv2.imshow('Image1', mask)
        cv2.waitKey(0)
        #detect circles in the image 
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 0.5, 41, param1=70, param2=15 , minRadius=0,maxRadius=175)
        #circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1.2 , 100)
        biggest = [0,0]
        index = 0
        #show all circles
        if circles is not None:
            for i in circles[0,:]:
                # draw the outer circle
                if i[2] > biggest[1]:
                    biggest[1] = i[2]
                    biggest[0] = index
                cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
                index += 1
            cv2.imshow("HoughCircles", img)
            cv2.waitKey()
        #show biggest circle
            final = cv2.circle(final,(circles[0,biggest[0]][0],circles[0,biggest[0]][1]),circles[0,biggest[0]][2],(0,255,0),2)
            cv2.imshow("HoughCircles", final)
            cv2.waitKey()
            cv2.destroyAllWindows()
            print(circles[0,biggest[0]][0])
        else: 
            print("error!") 
            cv2.destroyAllWindows()

circle = findcircle(imagepath)
print(circle)


        
