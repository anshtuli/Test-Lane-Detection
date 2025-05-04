import cv2
import numpy as np
import matplotlib.pyplot as plt

def Imgprocessing(i):
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
 
  

image=cv2.imread("Testimage.png")
lane_image=np.copy(image)
gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
edges=Imgprocessing(lane_image)
processedimg=ROI(edges)
lines=cv2.HoughLinesP(processedimg, 2, np.pi/180, 100, np.array([]), 80, 5)
lineimg=Display(lane_image,lines)
final_img=cv2.addWeighted(lane_image,0.8, lineimg,1,1)

cv2.imshow("Gray Test Image",gray)
cv2.waitKey(0)

cv2.imshow("Edge Test Image",edges)
cv2.waitKey(0)

plt.imshow(edges)
plt.title("Matplot")
plt.show()

cv2.imshow("Line Test Image",lineimg)
cv2.waitKey(0)

cv2.imshow("Final Test Image",final_img)
cv2.waitKey(0)