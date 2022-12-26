# 머신러닝, DNN, CNN 방법을 사용한 악기 소리 분류

## 1. wav file을 array 형태로 load

### librosa.load

    Logistic Regression : accuracy 4%
    Support Vector Machine : accuracy 6%
    Decision Tree : accuracy 32%

    data 길이(88200)가 너무 길기 때문에 성능이 제대로 나오지 않음.

## 2-1. Constant-Q 변환을 이용한 머신러닝 분류

### librosa.cqt

    Logistic Regression : accuracy 25%
    Support Vector Machine : accuracy 43%
    Decision Tree : accuracy 69%

    data 길이(14616)가 줄어들었기 때문에 성능이 올라감.

## 2-2. Constant-Q 변환을 이용한 딥러닝(DNN) 분류

![image](https://user-images.githubusercontent.com/103994779/209523348-1233265f-2b1e-4dc9-86bb-a99cca015012.png)
![image](https://user-images.githubusercontent.com/103994779/209523509-7c0e788c-a0b8-4ec1-86b6-7b110d1de33d.png)

    overfitting 되었다.
    accuracy : 35%

## 2-3. Constant-Q 변환을 이용한 딥러닝(CNN) 분류

![image](https://user-images.githubusercontent.com/103994779/209523796-36646d24-6476-4007-9a61-da99b476dba3.png)
![image](https://user-images.githubusercontent.com/103994779/209523862-003d4d25-3765-4714-94c4-40de679d9b63.png)

    마지막에 overfitting 되는 경향을 보이지만 성능이 매우 올라감.
    accuracy : 93%

## 3-1. MFCC를 이용한 머신러닝 분류

### librosa.feature.mfcc

    Logistic Regression : accuracy 92%
    Support Vector Machine : accuracy 97%
    Decision Tree : accuracy 80%

    data 길이(3460)가 매우 줄어들었기 때문에 성능이 올라감.

## 3-2. MFCC를 이용한 딥러닝(DNN) 분류

![image](https://user-images.githubusercontent.com/103994779/209524332-e884315e-dd7f-42dc-878c-a31863c8156d.png)
![image](https://user-images.githubusercontent.com/103994779/209524382-0db7a70d-9d30-4de5-8e3c-391058eb0fdb.png)

    Constant-Q 변환에 비해 성능이 올라감.
    accuracy : 88%

## 3-3. MFCC를 이용한 딥러닝(CNN) 분류

![image](https://user-images.githubusercontent.com/103994779/209524670-7573dfd3-9df0-4fc8-8c72-85c347b5a706.png)
![image](https://user-images.githubusercontent.com/103994779/209524706-92ee419d-e59a-465b-99c3-2d18359fa6ee.png)

    성능이 매우 좋다.
    accuracy : 98%

## 4. Conclusion

    - audio file을 librosa library를 사용해 간단히 array 형태로 변환할 수 있었고 변환된 array를 이용해 다양한 방법(머신러닝, DNN, CNN)으로 결과를 예측해 볼 수 있었다.
    - 같은 data일지라도 어떤 model을 쓰는 지에 따라 다른 결과가 나왔고 머신러닝 -> DNN -> CNN으로 갈 수록 성능이 좋아지는 결과를 보였다.
    - 같은 model을 쓴 경우에는 audio file을 어떤 data 형태로 변환하는 지에 따라 예측 결과에 큰 차이를 보였다.
    - 단순히 array 형태로 load 했을 경우에는 결과값이 매우 좋지 않았지만, Constant-Q, MFCC를 이용해 data를 변환했을 때는 예측 성능이 매우 높아지는 결과를 나타내었다.
    - data에 맞는 좋은 model을 쓰는 것도 중요하지만, data를 제대로 전처리하는 것이 예측 결과 향상에 큰 영향을 준다는 것을 다시 한번 느끼게 된 project 였다.
