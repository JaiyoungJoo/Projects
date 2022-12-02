import cv2
import time
import PoseModule2 as pm
import math

# right
# 점14를 기준으로 (12 - 14) (16 - 14) 이렇게 하면 벡터 2개가 나옴.
def degree(img, lmList):
    if len(lmList) != 0 :
        # 벡터 구하기
        rightarm_v1 = (lmList[12][1]-lmList[14][1], lmList[12][2]-lmList[14][2])
        rightarm_v2 = (lmList[16][1]-lmList[14][1], lmList[16][2]-lmList[14][2])
        # 각 벡터 길이 구하기
        d1 = math.sqrt((lmList[12][1]-lmList[14][1])**2 + (lmList[12][2]-lmList[14][2])**2)
        d2 = math.sqrt((lmList[16][1]-lmList[14][1])**2 + (lmList[16][2]-lmList[14][2])**2)
        # 두 벡터 사이 점곱
        v1v2 = (lmList[12][1]-lmList[14][1])*(lmList[16][1]-lmList[14][1]) + (lmList[12][2]-lmList[14][2])*(lmList[16][2]-lmList[14][2])
        c = v1v2/(d1*d2)
        print(d1)
        print(d2)
        print(v1v2)
        print(d1*d2)
        print(c)
        rad = math.acos(c)

        PI = math.pi
        deg = (rad*180)/PI
        deg = int(deg)
        cv2.putText(img, str(deg)+'degree', (200, 200), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
    return img
