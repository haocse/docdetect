import cv2
import docdetect
import numpy as np
import urllib.request
url='http://172.16.50.57:8080/shot.jpg'


# video = cv2.VideoCapture(video_path)
cv2.startWindowThread()
cv2.namedWindow('output')
while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    # ret, frame = video.read()
    rects = docdetect.process(frame)
    frame = docdetect.draw(rects, frame)
    cv2.imshow('output', frame)
    cv2.waitKey(1)
video.release()