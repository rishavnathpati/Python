import cv2
 
# Opens the Video file
cap= cv2.VideoCapture('/home/rishav/Desktop/Python/Video Summarization/sample.mpg')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('/home/rishav/Desktop/Python/images/frame'+str(i)+'.jpg',frame)
    print("Writing frame",i)
    i+=1
 
cap.release()
cv2.destroyAllWindows()