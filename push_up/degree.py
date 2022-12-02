import cv2
import time
import PoseModule2 as pm
import math

# right
# 점14를 기준으로 (12 - 14) (16 - 14) 이렇게 하면 벡터 2개가 나옴.
def degree(img, lmList, width, height, view):
    
    if len(lmList) != 0 :
        if view == 'right':
            # 벡터 구하기
            rightarm_v1 = (lmList[12][1]-lmList[14][1], lmList[12][2]-lmList[14][2])
            rightarm_v2 = (lmList[16][1]-lmList[14][1], lmList[16][2]-lmList[14][2])
            # 각 벡터 길이 구하기
            d1 = math.sqrt((lmList[12][1]-lmList[14][1])**2 + (lmList[12][2]-lmList[14][2])**2)
            d2 = math.sqrt((lmList[16][1]-lmList[14][1])**2 + (lmList[16][2]-lmList[14][2])**2)
            # 두 벡터 사이 점곱
            v1v2 = (lmList[12][1]-lmList[14][1])*(lmList[16][1]-lmList[14][1]) + (lmList[12][2]-lmList[14][2])*(lmList[16][2]-lmList[14][2])

            # cos값 구하기
            c = v1v2/(d1*d2)

            # cos값으로 radian값 구하기
            rad = math.acos(c)
            PI = math.pi
            deg = (rad*180)/PI
            deg = int(deg)

            # 영상 우상단에 text
            cv2.putText(img, 'rightarm'+str(deg), (int(width-400), 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
            cv2.putText(img, 'degree', (int(width-200), 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)

        elif view == 'left':
            # 벡터 구하기
            leftarm_v1 = (lmList[11][1]-lmList[13][1], lmList[11][2]-lmList[13][2])
            leftarm_v2 = (lmList[15][1]-lmList[13][1], lmList[15][2]-lmList[13][2])
            # 각 벡터 길이 구하기
            d1 = math.sqrt((lmList[11][1]-lmList[13][1])**2 + (lmList[11][2]-lmList[13][2])**2)
            d2 = math.sqrt((lmList[15][1]-lmList[13][1])**2 + (lmList[15][2]-lmList[13][2])**2)
            # 두 벡터 사이 점곱
            v1v2 = (lmList[11][1]-lmList[13][1])*(lmList[15][1]-lmList[13][1]) + (lmList[11][2]-lmList[13][2])*(lmList[15][2]-lmList[13][2])

            # cos값 구하기
            c = v1v2/(d1*d2)

            # cos값으로 radian값 구하기
            rad = math.acos(c)
            PI = math.pi
            deg = (rad*180)/PI
            deg = int(deg)

            # 영상 우상단에 text
            cv2.putText(img, 'leftarm'+str(deg), (int(width-400), 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
            cv2.putText(img, 'degree', (int(width-200), 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
    return img
