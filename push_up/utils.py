import cv2
import time
import math




def score(img, armdeg, bodydeg, width, stack,armscore, num):

    # down position
    if stack == 1 and armdeg <= 90:
        armscore2 = 150 - armdeg
        if armscore2 > armscore:
            armscore = armscore2
    else:
        armscore = armscore

    cv2.putText(img, f'score:{int(armscore):3d}', (int(width-430), 150), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)

    return img, armscore, num

def direction(img, lmList, view):
    
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
            if (rightarm_d1*rightarm_d2) != 0:
                arm_c = v1v2/(rightarm_d1*rightarm_d2)
            
                # cos값으로 radian값 구하기
                arm_rad = math.acos(arm_c)
                PI = math.pi
                arm_deg = (arm_rad*180)/PI
                arm_deg = int(arm_deg)
                armdeg = arm_deg
            else:
                armdeg = armdeg

            # 영상 우상단에 text
            # cv2.putText(img, f'arm{int(arm_deg):3d}', (int(width-400), 50), cv2.FONT_HERSHEY_PLAIN, 3,
            #             (255, 0, 0), 3)
            # cv2.putText(img, 'degree', (int(width-200), 50), cv2.FONT_HERSHEY_PLAIN, 3,
            #             (255, 0, 0), 3)

            # ===rightbody 12번, 24번, 26번===
            # 각 벡터 길이 구하기
            body_d1 = math.sqrt((lmList[12][1]-lmList[24][1])**2 + (lmList[12][2]-lmList[24][2])**2)
            body_d2 = math.sqrt((lmList[26][1]-lmList[24][1])**2 + (lmList[26][2]-lmList[24][2])**2)
            
            # 두 벡터 사이 점곱
            bodyv1v2 = (lmList[12][1]-lmList[24][1])*(lmList[26][1]-lmList[24][1]) + (lmList[12][2]-lmList[24][2])*(lmList[26][2]-lmList[24][2])

            # cos값 구하기
            if (body_d1*body_d2) != 0:
                body_c = bodyv1v2/(body_d1*body_d2)
            
                # cos값으로 radian값 구하기
                rad = math.acos(body_c)
                PI = math.pi
                deg = (rad*180)/PI
                deg = int(deg)
            else:
                bodydeg = deg
            

            # 영상 우상단에 text
            # cv2.putText(img, f'body{int(deg):3d}', (int(width-430), 100), cv2.FONT_HERSHEY_PLAIN, 3,
            #             (255, 0, 0), 3)
            # cv2.putText(img, 'degree', (int(width-200), 100), cv2.FONT_HERSHEY_PLAIN, 3,
            #             (255, 0, 0), 3)
                            
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
            if (d1*d2) != 0:
                c = v1v2/(d1*d2)

                # cos값으로 radian값 구하기
                rad = math.acos(c)
                PI = math.pi
                deg = (rad*180)/PI
                arm_deg = int(deg)
                armdeg = arm_deg
            else:
                armdeg = armdeg

            # 영상 우상단에 text
            # cv2.putText(img, 'arm'+str(arm_deg), (int(width-400), 50), cv2.FONT_HERSHEY_PLAIN, 3,
            #             (255, 0, 0), 3)
            # cv2.putText(img, 'degree', (int(width-200), 50), cv2.FONT_HERSHEY_PLAIN, 3,
            #             (255, 0, 0), 3)

            # ===leftbody 11번, 23번, 25번===
            # 각 벡터 길이 구하기
            body_d1 = math.sqrt((lmList[11][1]-lmList[23][1])**2 + (lmList[11][2]-lmList[23][2])**2)
            body_d2 = math.sqrt((lmList[25][1]-lmList[23][1])**2 + (lmList[25][2]-lmList[23][2])**2)
            # 두 벡터 사이 점곱
            bodyv1v2 = (lmList[11][1]-lmList[23][1])*(lmList[25][1]-lmList[23][1]) + (lmList[11][2]-lmList[23][2])*(lmList[25][2]-lmList[23][2])

            # cos값 구하기
            if (body_d1*body_d2) != 0:
                body_c = bodyv1v2/(body_d1*body_d2)

                # cos값으로 radian값 구하기
                rad = math.acos(body_c)
                PI = math.pi
                deg = (rad*180)/PI
                deg = int(deg)
                bodydeg = deg
            else:
                bodydeg = bodydeg

            # 영상 우상단에 text
            # cv2.putText(img, f'body{int(deg):3d}', (int(width-430), 100), cv2.FONT_HERSHEY_PLAIN, 3,
            #             (255, 0, 0), 3)
            # cv2.putText(img, 'degree', (int(width-200), 100), cv2.FONT_HERSHEY_PLAIN, 3,
            #             (255, 0, 0), 3)

    return img, armdeg, bodydeg

def count(img, armdeg, bodydeg, stack, num, armscore):

    if armdeg <= 90 and stack == 0:
        stack = 1
    elif armdeg >= 160 and stack == 1:
        num += 1
        armscore = 0
        stack = 0
        
    cv2.putText(img, f'count:{num}, stack:{stack}', (20, 150), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    return img, num, stack, armscore