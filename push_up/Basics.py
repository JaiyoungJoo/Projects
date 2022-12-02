import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

# cap = cv2.VideoCapture('federer.mp4')
cap = cv2.VideoCapture('perfect_push_up.mp4')
# cap = cv2.VideoCapture(0)
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks) 이걸로 x,y,z 좌표를 찍는다.
    if results.pose_landmarks:
        # mpDraw.draw_landmarks(img, results.pose_landmarks) 이렇게만 하면 점만 찍힌다.
        # https://google.github.io/mediapipe/solutions/pose.html 여기에 점 좌표 나와있다.
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        # id에 점 숫자가 들어감. lm 이 좌표 위치임
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            # lm.x * w 이게 실제 픽셀 위치임
            cx, cy = int(lm.x * w), int(lm.y * h)
            # 좌표에 원 그림 넣기
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(10) == 27:
        break
    # cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()