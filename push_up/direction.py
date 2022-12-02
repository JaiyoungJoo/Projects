import cv2
import time
import PoseModule2 as pm
import math

# check right or left direction

def direction(img, lmList, view):
    view = ''
    if len(lmList) != 0 :
        if lmList[12][1] > lmList[24][1]:
            cv2.putText(img, str('right view'), (20, 100), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
            view = 'right'

        else:
            cv2.putText(img, str('left view'), (20, 100), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
            view = 'left'
            
    return img, view





