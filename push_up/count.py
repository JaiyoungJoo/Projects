import cv2

'''
count 기준
- 팔이 100도 보다 밑으로 내려갈 것
- 팔이 160도보다 펴질 것

count +1 할 때 score 초기화
'''
def count(img, armdeg, bodydeg, stack, num, armscore):


    if armdeg <= 100 and stack == 0:
        stack = 1
    elif armdeg >= 160 and stack == 1:
        num += 1
        armscore = 0
        stack = 0

        
        
    cv2.putText(img, f'count:{num}, stack:{stack}', (20, 150), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    return img, num, stack, armscore

    