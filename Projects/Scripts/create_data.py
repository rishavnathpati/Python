# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:29:39 2020

@author: Rishav Nath Pati
"""

# This code basically creates the database for your face using the webcam of your laptop It captures images and
# stores them in a the folder named datasets under the folder name of sub_data(basically the name of y)

import cv2
import os

haar_file = 'haarcascade_frontalface_default.xml'

# All the faces data will be 
#  present this folder 
datasets = 'datasets'

# These are sub data sets of folder,  
# for my faces I've used my name you can  
# change the label here 
sub_data = 'rishav'

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)

# defining the size of images  
(width, height) = (130, 100)

# '0' is used for my webcam,
# if you've any other camera 
#  attached use '1' like this 
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

# The program loops until it has 30 images of the face. 
count = 0
while count < 20:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('% s/% s.png' % (path, count), face_resize)
    count += 1

    cv2.imshow('OpenCV', im)
    im = webcam.read()
    key = cv2.waitKey(20)
    if key == 27:
        break
cv2.destroyWindow("OpenCV")
webcam.release()
