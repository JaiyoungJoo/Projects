import cv2
import time
import PoseModule2 as pm
import direction 
import degree
# import score

# 함수 main에 있는 부분 그대로 복붙

cap = cv2.VideoCapture('perfect_push_up.mp4')
# cap = cv2.VideoCapture('leftpushup.mp4')
# cap = cv2.VideoCapture('rightpushup.mp4')
# cap = cv2.VideoCapture('only_federer.avi')

pTime = 0

# 이거 pm. 해야 함.

detector = pm.poseDetector()

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

cnt = 0
while True:
    cnt+=1
    success, img = cap.read()

    if not success:
        break
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    # lmList = detector.findPosition(img, draw=True)
    if len(lmList) !=0:
        # print(lmList)
        print('========================')
        # cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    # cv2.putText(img, str(int(cnt)), (200, 100), cv2.FONT_HERSHEY_PLAIN, 3,
    #             (255, 0, 0), 3)

    # cv2.imshow("Image", img)
    # cv2.waitKey(1)
    # img2 = img[200:, 100:600]
    view=''
    armdeg = 0
    bodydeg = 0
    img, view = direction.direction(img, lmList, view)
    img, armdeg, bodydeg = degree.degree(img, lmList, width, height, view, armdeg, bodydeg)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(10) == 27:
        break
    # cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()