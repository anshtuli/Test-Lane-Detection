import cv2
import numpy as np

def Imgprocessing(i):
 gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
 edges = cv2.Canny(gray, threshold1=50, threshold2=150)
 return edges

def ROI(i):
 h=i.shape[0]
 triangle=np.array([[(160,h),(720,h),(430,360)]])
 mask=np.zeros_like(i)
 cv2.fillPoly(mask,triangle,255)
 maskedimg=cv2.bitwise_and(i,mask)
 return maskedimg

def Display(i,l):
 line=np.zeros_like(i)
 if l is not None:
  for x in l:
   x1,y1,x2,y2=x.reshape(4)
   cv2.line(line, (x1,y1), (x2,y2), (0,0,255), 10)
 return line
 
capture=cv2.VideoCapture("Testvideo.mp4")
while (capture.isOpened()):
 ret,frame=capture.read()
 if not ret:
        print("Error: Frame not read properly.")
        break
 edges=Imgprocessing(frame)
 processedimg=ROI(edges)
 lines=cv2.HoughLinesP(processedimg, 2, np.pi/180, 100, np.array([]), 30, 10)
 lineimg=Display(frame,lines)
 final_vid=cv2.addWeighted(frame,0.8, lineimg,1,1)
 cv2.imshow("Final Test video",final_vid)
 if cv2.waitKey(1)==ord('e'):
   break
