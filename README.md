
# Project AIFFELTHON


<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=Android&logoColor=white"> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white"> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white">

## 💡프로젝트 소개
```
1️⃣ 주제 : 신체 검사 결과로 영양 상태 분석 후 영양 성분 추천   
2️⃣ 데이터셋 : 건강보험공단 - 건강검진결과 데이터   
3️⃣ 전처리 : AST, ALT, 혈색소, 공복혈당, 키, 몸무게만 사용   
4️⃣ 모델 : SVM, 추천 시스템   
5️⃣ 간단 설명 : 신체 검사 결과 자료에서 필요한 데이터만 추출한 후 SVM을 통해 1차 분류를 한다. 분류된 데이터로 추천시스템 로직을 통해 필요한 영양제를 추천한다.
```


---
## 🤸‍♂️ 팀 소개

### 💪슬기로운 건강생활💪

|이봄|이슬기|이호빈|홍연수|
|---|---|---|---|
|![image](https://user-images.githubusercontent.com/96757866/166195163-f7f405d5-fa8d-44b7-9d79-2e2dcf6a1ebb.png)|![image](https://user-images.githubusercontent.com/96757866/166195149-bc89383e-ddf7-48d3-a1d6-db79bed4d4aa.png)|![image](https://user-images.githubusercontent.com/96757866/166195189-2ffa50c4-a94d-4c19-a396-a5ee8f89b642.png)|![image](https://user-images.githubusercontent.com/96757866/166195108-3464148f-8cff-4f95-8ca5-a5e78a07d2e0.png)|
|- 문서 관리 </br>- 데이터 가공 </br>-UI디자인|- 총괄 </br>-모델링|- 데이터셋 탐색 </br> - 데이터 EDA|- 논문 자료 수집 및 정리 </br>- 모델링|
|앞만 보고 가겠습니다..!|일을 저질렀으니 수습해야 인간이죠ㅎ|후퇴는 없다..|한번 해 보겠습니다|

---
## 🏅 프로젝트 목표
#### 1. SVM accuracy 95% 이상
#### 2. 추천 시스템 구현
#### 3. 사용자 화면으로 알고리즘 실행

---
## 🗓️ 프로젝트 일정
- 해당 일정은 프로젝트 진행에 따라 수정된다.

|내용|M1|M2|H1|H2|H3|H4|H5|H6|
|---|---|---|---|---|---|---|---|---|
|데이터셋 탐색|🟡||||||||
|데이터 분석||🟡|||||||
|데이터 EDA||🟡|||||||
|프로세스 이해||🟡|||||||
|모델 선정|||🟡||||||
|모델 구축||||🟡|🟡|🟡|||
|결과 분석|||||||🟡||
|UI 디자인||||||||🟡|
|앱서버 연결||||||||🟡|

---
## 🤖 모델 사용
### 선정 모델 : SVM, 추천시스템
### 선정 이유 : 
1. 기본적으로 SVM같은 경우에는 광범위하게 사용되는 지도학습의 일종으로 패턴을 인지하고 분류 문제에 있어서 강력한 툴이다. 

2. BMI지수나 간수치, 혈색소 수치등 건강 수치는 기준점은 있지만, 단편 일률적인 판별을 하기에는 다차원적으로 분류를 하는 것이 필요하다. (병을 판단하기 위해서 묶여 있는 지표들이 많고 다차원적으로 여러 지표를 보고 건강유무를 판단한다.) 

3. 건강 지표로 환자로 의심되는 군과 정상인으로 판별되는 군을 나누어 거기에 맞는 건기식 추천을 해야하는 시스템으로  어떤 사람이 한 영화를 좋아했다면, 비슷한 콘텐츠의 아이템을 추천하는 방식인 Content based filtering 보다는  잠재요인 기법을 활용하는 Collaborative filtering가 적절하다고 판단하였고, baseline code로는 Collaborative filtering의 하위 범주인 user-based filtering의 베이스라인 코드를 선정하였다. 
### 👉 [SVM 베이스 코드 바로가기](https://github.com/LAGABI44/Project-AIFFELTHON/tree/main/Base%20code/SVM)
### 👉 [추천시스템 베이스 코드 바로가기](https://github.com/LAGABI44/Project-AIFFELTHON/tree/main/Base%20code/Recommender_system)
---
## 🦄 프로젝트를 위한 자료
#### [1. 데이터셋(국민건강보험공단)](https://www.data.go.kr/data/15007122/fileData.do)
#### [2. 논문 자료 바로가기](https://github.com/LAGABI44/Project-AIFFELTHON/tree/main/%EB%85%BC%EB%AC%B8%20%EC%9E%90%EB%A3%8C)
#### 3. 의료데이터 전처리
#### 4. 의료데이터 모델링

---
## 🏆 결과
👉 아래 영상 자동재생됩니다.   
![result](https://user-images.githubusercontent.com/96757866/172508654-841acd97-3f88-4233-a2cc-a5a8cd5828c0.gif)
