import cv2

def count(img, armdeg, bodydeg, stack, num):
    # if stack == -1 and armdeg <= 90:
    #     stack = 0

    if armdeg <= 90 and stack == 0:
        stack = 1
    elif armdeg >= 160 and stack == 1:
        num += 1
        stack = 0

        
        
    cv2.putText(img, f'count:{num}+stack:{stack}', (20, 150), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    return img, num, stack

    