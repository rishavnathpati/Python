import cv2

cv2.namedWindow("Preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
while rval:
    # noinspection PyUnboundLocalVariable
    cv2.imshow("Preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:
        break
cv2.destroyWindow("Preview")
vc.release()
