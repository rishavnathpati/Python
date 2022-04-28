# Face-recognition-using-OpenCV
This is my very first, trivial yet interesting project using python and OpenCV, where I have trained my program to recognise a set of faces all in real time. It uses the webcam to first record a set of images of a face, trains using those images with the help of harrcascade classifier, and then recognise those trained faces in real-time from the video feed obtained from webcam.

How to use it:
1. You will need to install opencv, and must have a webcam. 
2. In the program named create_data.py, enter the name of the person whose face you want to train in line 23.
3. You may train multiple faces, just change the name of the string assigned to sub_data in line 23.
4. After the training is complete, head over to the second program and run it. A window will pop up and will recognise the faces that you have trained, in real time, from your webcam. 

Approach/Algorithms used:
This project uses LBPH (Local Binary Patterns Histograms) Algorithm to detect faces. It labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.
LBPH uses 4 parameters :
(i) Radius: the radius is used to build the circular local binary pattern and represents the radius around the
central pixel.
(ii) Neighbors : the number of sample points to build the circular local binary pattern.
(iii) Grid X : the number of cells in the horizontal direction.
(iv) Grid Y : the number of cells in the vertical direction.
The model built is trained with the faces with tag given to them, and later on, the machine is given a test data and machine decides the correct label for it.

And please skip the datasets/rishav folder if you ever download this, contains some embarasing pictures of mine. 
Peace

