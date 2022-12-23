# Push-up count

## 프로젝트 기간

- 2022.12.02 ~ 22.12.22

## 프로젝트 인원

- 총 1명

## 프로젝트 내용

- Human skeleton detection model을 사용한 Push-up count model 만들기
- Push-up 시험 등에서 사용할 수 있도록 정해진 규칙에 따라 객관적으로 횟수를 count하도록 model 구현

## 프로젝트 진행

- 주제 선택
  - 기초적이고 체력 검정에 많이 쓰이는 Push-up 선택
- Human skeleton detection 조사
  - 다양한 model 중 성능이 좋고 많은 기능이 있는 Google mediapipe pose API 선택
  - https://google.github.io/mediapipe/solutions/pose.html
- Google Mediapipe pose model 확인
  - 총 33개의 pose landmarks를 detection
  - 겹치는 부분을 제외하고 정확한 landmarks를 predict함
- Push-up view, count, score 함수 구현
  - 팔, 다리 X 좌표를 기준으로 영상의 좌,우를 판단
  - 팔의 각도가 90˚이하로 굽혀질 때, 팔의 각도가 160˚이상 펴질 때 count
    - 영상 첫 3frame은 pose detection이 제대로 되지 않아 count 하지 않음
  - 팔의 각도가 많이 굽혀질 수록 score가 증가
- sample 영상 확인
  ![image](https://user-images.githubusercontent.com/103994779/209271508-af5923be-41c2-4372-82a2-d25493424854.png)
  ![image](https://user-images.githubusercontent.com/103994779/209271643-9c154c86-d9b3-4862-a507-07c4a7677622.png)

<!-- <img src="https://user-images.githubusercontent.com/103994779/209259695-4a2081e3-96ad-4aac-a396-b49748d1254b.png" width="500" height="400"/>  -->
