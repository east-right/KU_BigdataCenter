# 창원시 제조데이터 경진대회

![image](https://user-images.githubusercontent.com/67576850/212618167-4038bf3b-5460-4222-9c26-19e509848772.png)




* 분석내용
  * 목표:센서 파형을 이용하여 정상 물품과 비정상 물품 분류
  * 활용툴: Python
  * 사용라이브러리: Tensorflow, pandas, sklearn 등


* 분석정의
  * Re_ID를 기준으로 학습데이터, 이상적인 파형데이터, test 데이터 존재
  * RE_ID를 기준으로 이상적인 파형과 얼마나 차이가 차이가 나는가가 핵심 
  * 각 시간의 차이와 파형의 첨도, 외도, 고점시간, 저저시간 학습에 사용

* 분석타임라인
  * 센서데이터 전처리
  * 데이터를 차분하여 정상성 만들기
  * train 데이터와 이상파형 데이터 빼기, 추가적인 파생변수 생성
  * 스케일링과 LGBM을 활용한 모델학습
  
* 성과와 느낀점
  * 시계열 데이터에 관하여 많은 공부가 되었다
  * 중간에 PCA/tsne 와 같은 차원축소 기법에 대해 공부함
  * 중간에 AUTO ENCODER를 사용해보기 위해 많은 공부를 하였다.
  * 학습된 모델을 저장하는 습관을 기르자


![슬라이드1](https://user-images.githubusercontent.com/67576850/211143242-643bd87e-87c8-4ba5-84ca-c275ac99b643.JPG)
![슬라이드2](https://user-images.githubusercontent.com/67576850/211143245-f47b88d3-1843-4f3b-9b3f-71153ad155a2.JPG)
![슬라이드3](https://user-images.githubusercontent.com/67576850/211143246-0a11ebc0-a9a8-4f0a-a4c8-49c263f67772.JPG)
![슬라이드4](https://user-images.githubusercontent.com/67576850/211143248-1aec8e9f-f60b-4d02-b6ac-f747db423ecf.JPG)
![슬라이드5](https://user-images.githubusercontent.com/67576850/211143249-0efa4c49-468d-449e-a920-6ffba2b8c951.JPG)
![슬라이드6](https://user-images.githubusercontent.com/67576850/211143250-add7e478-abaf-460f-8601-6b4d0156d8dc.JPG)
![슬라이드7](https://user-images.githubusercontent.com/67576850/211143251-f4f58b8b-539d-4aa8-a789-bd42ac7aa3b0.JPG)
![슬라이드8](https://user-images.githubusercontent.com/67576850/211143252-c0700a24-0857-498f-9046-f2ec37ebbbfb.JPG)
![슬라이드9](https://user-images.githubusercontent.com/67576850/211143253-d4136320-2d77-4197-9487-0de357ca9f28.JPG)
![슬라이드10](https://user-images.githubusercontent.com/67576850/211143254-b48d408d-43ef-4a62-bc3b-2c62fdb199a9.JPG)
![슬라이드11](https://user-images.githubusercontent.com/67576850/211143255-22639030-236e-446f-b42a-cb2bfab4b72b.JPG)
