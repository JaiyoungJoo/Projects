import cv2
import time

video = cv2.VideoCapture('perfect_push_up.mp4')		
					
prev_time = 0
# FPS 의미 : 1초당 프레임 수 
# 1초 당 10frame이 지나간다는 뜻
# 1/FPS : 10frame 당 시간
FPS = 300

frame_cnt = 0
while True:
	
    ret, frame = video.read()
    frame_cnt += 1

    # time.time() 이거 하면 그냥 현재 시간을 나타냄
    # current_time 현재 시간과 이전 시간의 차이
    current_time = time.time() - prev_time
    # while을 계속 돌면서 만약 current_time이 10frame 당 시간보다 크면 영상 출력
    if ret:

        # 이전 시간 계속 리셋
        prev_time = time.time()

        cv2.putText(frame, str(int(frame_cnt)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
        cv2.imshow('video', frame)

        # 입력 대기 시간 10ms
        # 0보다 큰 키보드 수 입력 시 영상 종료
        if cv2.waitKey(10) > 0:
            break