개인 블로그 주소

https://joosblog.tistory.com/15?category=1037091
- .py 파일을 쓰는 법에 대해 배우기 전이라 주피터노트북으로 작성.
- pdf 파일 다운로드 https://github.com/JaiyoungJoo/portfolio/files/9651659/Cancerclassification_JOO.pdf
***
# 1. Overview
- 갑상선 초음파 사진을 이용하여 딥러닝 모델을 학습 시킨 후 종양(tumor)이 양성(benign)인지, 악성(malignant)인지 구분해 본다.
- 다양한 모델을 학습시킨 후 accuracy를 비교한다.
- 총 5가지 모델(EfficientNetB7, VGG16, VGG19, ResNet50, ResNet101)을 사용
# 2. Dataset
- before cropped
  - TRAIN 폴더 안에 Benign, Cancer 폴더가 있으며 각각 9004개 이미지, 2389개의 이미지가 있다.
  - TEST 폴더 안에 Benign, Cancer 폴더가 있으며 각각 899개 이미지, 267개의 이미지가 있다.
  - 각 이미지의 파일명은 (B_001-0002-1.0.jpg) 와 같이 맨 앞에 B, M으로 labelling 되어 있으며 그 뒤는 숫자로 이루어져 있다.
  - 모든 파일은 .jpg 형식이다.
- after cropped
  - cropped된 이미지 파일
  - dataset의 종양 부분만 잘라서 만든 이미지
  - Train2 폴더 안에 Benign, Cancer 폴더가 있으며 각각 7324개 이미지, 1624개의 이미지가 있다.
  - Test2 폴더 안에 Benign, Cancer 폴더가 있으며 각각 1831개 이미지, 406개의 이미지가 있다.
  - 각 이미지의 파일명은 (B_001-0002-1.0.jpg) 와 같이 맨 앞에 B, M으로 labelling 되어 있으며 그 뒤는 숫자로 이루어져 있다.
  - 모든 파일은 .jpg 형식이다.
