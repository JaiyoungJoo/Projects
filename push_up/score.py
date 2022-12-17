import cv2
import time
import PoseModule2 as pm

'''
score 기준
- 카운트가 1 증가하는 순간 score를 0으로 만들자.
- stack = 1 다운 상태
- stack = 0 업 상태
- (다운)팔의 경우 90도 이상으로 꺽이면 100점
- 카운트는 100부터 시작
- 팔 100도 ~ 50도 : 50점 ~ 100점

- (미구현)
- 올라올 경우는 score 계산하지 않음.
- 몸의 경우 어깨, 엉덩이, 무릎이 90도가 되면 0점
- 몸의 경우 어깨, 엉덩이, 무릎이 180도가 되면 0점
- (업)팔의 경우 170도 이상으로 꺽이면 100점
- 팔 160 이상 꺽여야 함.
- 팔 160 ~ 180도 : 50점 ~ 100점
'''
def score(img, armdeg, bodydeg, width, stack,armscore, num):

    # down position
    if stack == 1 and armdeg <= 100:
        armscore2 = 150 - armdeg
        if armscore2 > armscore:
            armscore = armscore2
    else:
        armscore = armscore

    cv2.putText(img, f'score:{int(armscore):3d}', (int(width-430), 150), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)

    return img, armscore, num