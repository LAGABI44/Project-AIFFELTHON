# 모델링(1)분류

#### 📑데이터셋 : [국민건강보험공단_혈압ㆍ혈당 데이터](https://www.data.go.kr/data/15095105/fileData.do)


#### 분류 모델 : SVM, Randomforest
---


## 진행상황

|No|날짜|이름|내용|
|---|---|---|---|
|01|---|이슬기|혈색소로 기본 SVM 모델 돌리기|
|02|22.05.03|이슬기|C값 찾기|
|03|22.05.04|이슬기|overfitting 검사 및 시각화|
|04|22.05.06|이슬기|로지스틱 회귀 및 f1-score 구하기|
|05|22.05.08|이슬기|7가지 모델 f1-score 비교|


---
#### 분류 모델 : SVM, SGDclassifier, Logistic Regression, Xgboost, LightGBM
---
## 진행상황

---
## 진행상황

|No|날짜|이름|내용|
|---|---|---|---|
|08, 09|22.05.19~22.05.30|이봄|LogisticRegression|


|No|날짜|이름|내용|
|---|---|---|-------------------|
|--|---|홍연수|추천시스템 시도 및 이진분류 모델링|
|--|22.04.20~22.05.03|홍연수|1.추천 시스템 (knowledge-based system) 공부 </br> 2. 추천 시스템 (user-based, item-based system),SVD 특잇값 분해 </br> 3.건기식 데이터가 있는 논문 서치|
|--|22.05.04~05.12|홍연수|랜덤 포레스트 모델링|
|01|22.05.13|홍연수|SVM 모델 진행중 (정확도 86%)|
|02|22.05.16|홍연수|SVM 하이퍼 파라미터 튜닝|
|03~05|22.05.17|홍연수|1.다른 모델로 시도함 (로지스틱회귀, SGD classifier) </br> 2. SVM 모델(3) </br> 3. SVM 모델(4)|
|06|22.05.18|홍연수|이진분류 모델링 & 모델 최적화|
|07|22.05.19|홍연수|ROC-AUC 커브 시각화, 하이퍼 파라미터 찾기(그리드 서치)| 
|10|22.05.23|홍연수|부스팅 계열 모델링 (Xgboost)|
|11|22.05.24|홍연수|Confusion matrix, data_iteration check(Xgboost)|
|12|22.05.26|홍연수|부스팅 계열 모델링(Xgboost)|
|13|22.05.30|홍연수|모델 총정리 및 stacking 시도|
|14|22.06.02|홍연수|LightGBM 진행 (LightGBM, Xgboost)|

선정 모델 : LightGBm

선정 이유 : boosting 계열의 모델의 성능이 좋게 나오는데, 그중에서도 XGboost는 무겁지만, LightGbm은 가볍고 성능지표 또한 XGboost 0.2 가량 높게 나와서 선정하게 됨



Reference)

https://github.com/lsjsj92/machine_learning_basic,

핸즈온 머신러닝 2판,

파이썬 머신러닝 완벽 가이드 2판 ,

혼자 공부하는 머신러닝 딥러닝









