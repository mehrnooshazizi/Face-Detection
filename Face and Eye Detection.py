# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:43:11 2020

@author: Azizi
"""
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_eye = cv2.CascadeClassifier('haarcascade_eye.xml')

cam = cv2.VideoCapture(0)
counter=1
while True:
    success, frame = cam.read()
    if success == True:
        resized_frame = cv2.resize(frame,(600,400))
        gray = cv2.cvtColor(resized_frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  
        for (x,y,w,h) in faces:
            newframe = cv2.rectangle(resized_frame,(x,y),(x + w, y + h),(0,255,0),2)           
            croped_frame = resized_frame[y: y + h, x: x + w]
            cv2.imwrite(f'G:/mehrnoosh/face{counter}.jpg',croped_frame)
            cv2.putText(frame,"Human",(x,y-10), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

            eyes = face_eye.detectMultiScale(croped_frame , 1.3, 6)             
            for (xe,ye,we,he) in eyes:
                frame = cv2.rectangle(croped_frame,(xe+x,ye+y),(xe + we+x, ye + he+y),(0,0,255),2)
                croped_frame1 = resized_frame[y: y + h, x: x + w]
                cv2.imwrite(f'G:/mehrnoosh/eye{counter}.jpg',frame)
                counter+=1
            cv2.imshow('myimage', frame)

    if cv2.waitKey(1) == 27 or counter==101:
        break

cam.release()
cv2.destroyAllWindows()
