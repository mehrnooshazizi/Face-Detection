# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:48:56 2020

@author: Azizi
"""
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_eye = cv2.CascadeClassifier('haarcascade_eye.xml')
def F1(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    if(faces == ()):
        return ()
    (x,y,w,h) = faces[0]
    cropped_image = gray[y:y + h, x:x + w]
    return cropped_image
cam = cv2.VideoCapture(0)
counter=1
while True:
    success, frame = cam.read()
    if success == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray , 1.3, 5)  
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
            face=F1(frame)
            
            faces = cv2.resize(frame,(200,200))
            cv2.imwrite(f'G:/mehrnoosh/face{counter}.jpg',faces)
            gray2 = gray[y:y+h,x:x+w]
            eyes = face_eye.detectMultiScale(gray2 , 1.3, 6) 
            cv2.putText(frame,"Human",(x,y-10), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            for (xe,ye,we,he) in eyes:
                frame = cv2.rectangle(frame,(xe+x,ye+y),(xe + we+x, ye + he+y),(0,0,255),2)
                cv2.imwrite(f'G:/mehrnoosh/eye{counter}.jpg',frame)
                counter+=1
            cv2.imshow('myimage', frame)

    if cv2.waitKey(1) == 27 or counter==101:
        break

cam.release()
cv2.destroyAllWindows()

