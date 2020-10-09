# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:40:50 2020

@author: Azizi
"""
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #load cascade


cam = cv2.VideoCapture(0) #capture or play video
counter = 1 # counter for count each detection
while counter < 200:
    status,frame = cam.read()
    if (status == True):
        resized_frame = cv2.resize(frame,(600,400)) #resize
        gray_frame = cv2.cvtColor(resized_frame,cv2.COLOR_BGR2GRAY) #gray
        faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5) #(frame, scale factor, min neighbours)
        for (x,y,w,h) in faces:
            detected_frame = cv2.rectangle(resized_frame,(x,y),(x + w,y + h),(0,255,255),1) #rectangle
            crop_img = resized_frame[y: y + h, x: x + w] # crop
            cv2.imwrite('G:/mehrnoosh' + str(counter) + '.jpg',crop_img,) #save
            cv2.putText(detected_frame,str(counter),(x,y - 10),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)# put text
            counter += 1 # add count
            cv2.imshow('my video',detected_frame) # show if detect

        cv2.imshow('my video',resized_frame) # show if not detect

    if (cv2.waitKey(1) == 27):
        break

cam.release()
cv2.destroyAllWindows()