# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Fri Feb 14 20:28:19 2020

@author: Grace Wu
"""
import cv2
import numpy as np
import imutils
import glob
import os
from pathlib import Path
import rospy
from std_msgs.msg import String

def findcircle(imagepath,level):
    imagepath = 'C:/Users/Grace Wu/m19/src/img/*.JPG'
    resizedw = 500
    resizedh = 375
    maxbluerad = 100
    maxredrad = 100
    maxgreenrad = 100
    tolerance = 5
    xaligned = False
    zaligned = False
    yaligned = False
    b = [np.array([60,90,90]), np.array([120,320,120]), maxbluerad]
    r = [np.array([60,90,90]), np.array([120,320,120]), maxredrad]
    g = [np.array([60,90,90]), np.array([120,320,120]), maxgreenrad]
    #declare ros node
    pubx = rospy.Publisher('xstuff', float32, queue_size=10)
    pubz = rospy.Publisher('zstuff', float32, queue_size=10)
    puby = rospy.Publisher('ystuff', float32, queue_size=10)
    rospy.init_node('circlecords', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #loop for each color
    colours = [b,r,g]
    for i in colours:
        #loop until all dimensions aligned
        while xaligned == False or zaligned == False or yaligned == False:
            #import image
            list_of_files = glob.glob(imagepath) # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            image = cv2.imread(latest_file)
            #make picture smaller
            resized = imutils.resize(image, width=resizedw)
            #make colour filter
            hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv,i[0],i[1])
            img = cv2.bitwise_and(resized, resized, mask=mask)
            cv2.imshow('Image1', mask)
            cv2.waitKey(0)
            final = resized.copy()
            #detect circles in the image 
            circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 0.5, 41, param1=70, param2=12 , minRadius=0,maxRadius=175)
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
                cv2.circle(final,(circles[0,biggest[0]][0],circles[0,biggest[0]][1]),circles[0,biggest[0]][2],(0,255,0),2)
                cv2.imshow("HoughCircles", final)
                cv2.waitKey()
                cv2.destroyAllWindows()
                #evaluate position
                if biggest[0][0] < resizedw/2 + tolerance and biggest[0][0] > resizedw/2 - tolerance:
                    xaligned = True
                if biggest[0][1] < resizedh/2 + tolerance and biggest[0][1] > resizedh/2 - tolerance:
                    zaligned = True
                if biggest[0][2] < i[2] + tolerance and biggest[0][2] > i[2] - tolerance:
                    yaligned = True
                #publish circle coordinates
                pubx.publish(circles[0,biggest[0]][0])
                pubz.publish(circles[0,biggest[0]][1])
                puby.publish(circles[0,biggest[0]][2])
                rate.sleep()
            else: 
                print("warning! no circles found") 
                pubx.publish(0)
                pubz.publish(0)
                puby.publish(0)
                rate.sleep()
                cv2.destroyAllWindows()

        
