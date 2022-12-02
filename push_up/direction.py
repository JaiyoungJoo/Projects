import cv2
import time
import PoseModule2 as pm
import math

# check right or left direction

def direction(img, lmList):
    
    if len(lmList) != 0 :
        if lmList[12][1] > lmList[28][1]:
            cv2.putText(img, str('right'), (100, 100), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
            
            
        else:
            cv2.putText(img, str('left'), (100, 100), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
            
            

    return img





