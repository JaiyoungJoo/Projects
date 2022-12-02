# Push up count model

I use this model.<br>
https://google.github.io/mediapipe/solutions/pose.html
![image](https://user-images.githubusercontent.com/103994779/204980438-299a34d8-7fd6-4b3a-9f2b-a19383313603.png)

## 1. How to detect Left or Right?

- Check hand and foot locations
  - Right side
    - joint(12) and joint(28)
    - If X-coordinate of joint(28) is located on the left side, it means camera watching right side of person.
    - In this case, only use joint num(16,14,12,26,28)
  - Left side
    - joint(11) and joint(27)
    - If X-coordinate of joint(27) is located on the left side, it means camera watching left side of person.
    - In this case, only use joint num(15,13,11,25,27)

## 2. How to count number of push-ups?

- Rigth side
  - Check angle between joint(12), joint(14) and joint(24).
    - If the angle is less than 90 degrees, it means push-down.
    - If the angle is greater than 170 degrees, it means push-up.
    - When person goes push-down first and goes push-up, model add push-up count.
