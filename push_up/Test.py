import cv2
import time
from Module import PoseModule3 as pm
import utils

# 함수 main에 있는 부분 그대로 복붙

cap = cv2.VideoCapture('sample_video/leftpushup.mp4')
# cap = cv2.VideoCapture('sample_video/rightpushup.mp4')
# cap = cv2.VideoCapture('perfect_push_up.mp4')

# To count FPS 
pTime = 0

# 이거 pm. 해야 함.
# 같은 폴더에 있는 PoseModule2.py에서 poseDetector class를 불러옴.
detector = pm.poseDetector()

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# push-down : stack=0 / push-up : stack = 1
stack=0

# frame count
cnt = 0

# number of push-up
num = 0 # 푸쉬업 횟수

# score : calculate from arm degree
armscore = 0

# direction of video : right or left
view=''

# To calculate arm degree and body degree
armdeg = 0
bodydeg = 0

while True:
    cnt+=1
    success, img = cap.read()

    if not success:
        break

    # draw=False : 선 안그림
    img = detector.findPose(img, draw=False)
    # draw=False : 점 안그림
    lmList = detector.findPosition(img, draw=False)
    
    # 좌표 print /  특정 좌표 점 그리기
    # if len(lmList) !=0:
        # print(lmList)
        # cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    # FPS 계산
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # FPS를 영상에 넣기
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    # 나중에 수정할 내용 - 함수를 하나로 합치기
    img, view = utils.direction(img, lmList, view)
    # 각도 계산 / 그리기
    if len(lmList) !=0 and view == 'left':
        armdeg = detector.findAngle(img, 15,13,11)
        bodydeg = detector.findAngle(img, 25,23,11)
    elif len(lmList) !=0 and view == 'right':
        armdeg = detector.findAngle(img, 12,14,16)
        bodydeg = detector.findAngle(img, 12,24,26)

    img, armdeg, bodydeg = utils.degree(img, lmList, width, height, view, armdeg, bodydeg)
    
    # 30프레임 이후 count 시작, 영상 처음 이상하게 detection함.
    # 30frame 이전 'Wait a second...' 출력
    if cnt >= 30:
        img, num, stack, armscore = utils.count(img, armdeg, bodydeg, stack, num, armscore)
        img, armscore, num = utils.score(img, armdeg, bodydeg, width, stack,armscore, num)
    else:
        cv2.putText(img, 'Wait a second...', (20, 150), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)

    # esc 누를 경우 영상 종료
    if cv2.waitKey(10) == 27:
        break
    # cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()