# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:04:22 2019

@author: paneesh
"""
import cv2 


# create cascade classifier obj
# Replace username with the system username 
face_cascade = cv2.CascadeClassifier("C:\\Users\\username\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

# read image
# enter the path of image as a parameter 
img = cv2.imread("paste Image path here", 1)


# read image as grey scale
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# search the co=ordinates of image 
faces = face_cascade.detectMultiScale(gry_img, scaleFactor = 1.05, minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)

resize = cv2.resize(img, (int (img.shape[1]/2), int (img.shape[0]/2)))

cv2.imshow("image", resize)

cv2.waitKey(0)

cv2.destroyAllWindows()
