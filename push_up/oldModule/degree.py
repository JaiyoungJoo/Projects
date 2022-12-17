import cv2
import time
import PoseModule2 as pm
import math

# right
# 점14를 기준으로 (12 - 14) (16 - 14) 이렇게 하면 벡터 2개가 나옴.
def degree(img, lmList, width, height, view, armdeg, bodydeg):
    
    if len(lmList) != 0 :
        if view == 'right':
            # ===rightarm 12번, 14번, 16번===
            # 각 벡터 길이 구하기
            rightarm_d1 = math.sqrt((lmList[12][1]-lmList[14][1])**2 + (lmList[12][2]-lmList[14][2])**2)
            rightarm_d2 = math.sqrt((lmList[16][1]-lmList[14][1])**2 + (lmList[16][2]-lmList[14][2])**2)
            
            # 두 벡터 사이 점곱
            v1v2 = (lmList[12][1]-lmList[14][1])*(lmList[16][1]-lmList[14][1]) + (lmList[12][2]-lmList[14][2])*(lmList[16][2]-lmList[14][2])

            # cos값 구하기
            arm_c = v1v2/(rightarm_d1*rightarm_d2)
            
            # cos값으로 radian값 구하기
            arm_rad = math.acos(arm_c)
            PI = math.pi
            arm_deg = (arm_rad*180)/PI
            arm_deg = int(arm_deg)

            # 영상 우상단에 text
            cv2.putText(img, f'arm{int(arm_deg):3d}', (int(width-400), 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
            cv2.putText(img, 'degree', (int(width-200), 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)

            # ===rightbody 12번, 24번, 26번===
            # 각 벡터 길이 구하기
            body_d1 = math.sqrt((lmList[12][1]-lmList[24][1])**2 + (lmList[12][2]-lmList[24][2])**2)
            body_d2 = math.sqrt((lmList[26][1]-lmList[24][1])**2 + (lmList[26][2]-lmList[24][2])**2)
            
            # 두 벡터 사이 점곱
            bodyv1v2 = (lmList[12][1]-lmList[24][1])*(lmList[26][1]-lmList[24][1]) + (lmList[12][2]-lmList[24][2])*(lmList[26][2]-lmList[24][2])

            # cos값 구하기
            body_c = bodyv1v2/(body_d1*body_d2)
            
            # cos값으로 radian값 구하기
            rad = math.acos(body_c)
            PI = math.pi
            deg = (rad*180)/PI
            deg = int(deg)

            # 영상 우상단에 text
            cv2.putText(img, f'body{int(deg):3d}', (int(width-430), 100), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
            cv2.putText(img, 'degree', (int(width-200), 100), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)

            armdeg = arm_deg
            bodydeg = deg

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
            arm_deg = int(deg)

            # 영상 우상단에 text
            cv2.putText(img, 'arm'+str(arm_deg), (int(width-400), 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
            cv2.putText(img, 'degree', (int(width-200), 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)

            # ===leftbody 11번, 23번, 25번===
            # 각 벡터 길이 구하기
            body_d1 = math.sqrt((lmList[11][1]-lmList[23][1])**2 + (lmList[11][2]-lmList[23][2])**2)
            body_d2 = math.sqrt((lmList[25][1]-lmList[23][1])**2 + (lmList[25][2]-lmList[23][2])**2)
            # 두 벡터 사이 점곱
            bodyv1v2 = (lmList[11][1]-lmList[23][1])*(lmList[25][1]-lmList[23][1]) + (lmList[11][2]-lmList[23][2])*(lmList[25][2]-lmList[23][2])

            # cos값 구하기
            body_c = bodyv1v2/(body_d1*body_d2)
            # cos값으로 radian값 구하기
            rad = math.acos(body_c)
            PI = math.pi
            deg = (rad*180)/PI
            deg = int(deg)

            # 영상 우상단에 text
            cv2.putText(img, f'body{int(deg):3d}', (int(width-430), 100), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
            cv2.putText(img, 'degree', (int(width-200), 100), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
            
            armdeg = arm_deg
            bodydeg = deg
    return img, armdeg, bodydeg
