# 한림대 헬스케어 헤커톤 대회

* 분석내용
  * 목표:제공된 보행데이터를 이용하여 정상보행자와 비정상 보행자 분류
  * 활용툴: Python
  * 사용라이브러리: Tensorflow, pandas, sklearn 등


* 분석정의
  * 제공 데이터 xyz를 기준으로 한 센서의 가속도 시계열 데이터 
  * 양손, 양발목, 허리를 기준으로 데이터 존재
  * 데이터를 3차원 array로 정의

* 분석타임라인
  * 센서데이터 전처리
  * 데이터 정규화 및 시각화
  * 5개의 1D-CNN 모델 구축 후 Concatenate
  * Concatenate한 모델 RNN으로 재구축 후 학습
  
* 성과와 느낀점
  * 데이터 분석에만 신경을 써서 EDA를 소홀히하였다.
  * Model Concatenate에 대해 많은 학습이 되었다.
  * 데이터 정의에 많이 미흡하였다.
  * 본 프로젝트를 통하여 시각화를 비롯한 EDA의 중요성에 대해 많이 깨달았다.


![슬라이드1](https://user-images.githubusercontent.com/67576850/211143145-4fef677e-c4ab-4e70-a03e-bc76d5274484.JPG)
![슬라이드2](https://user-images.githubusercontent.com/67576850/211143147-c021f83b-5b86-4cc8-88cb-6a018061f226.JPG)
![슬라이드3](https://user-images.githubusercontent.com/67576850/211143148-62c52cc9-5c58-4d1c-918e-6aa77cd4bee6.JPG)
![슬라이드4](https://user-images.githubusercontent.com/67576850/211143150-bf137310-ba5b-4019-82c3-0261c15e12fe.JPG)
![슬라이드5](https://user-images.githubusercontent.com/67576850/211143151-456fbc14-cd1b-468f-9845-0143fad03d22.JPG)
![슬라이드6](https://user-images.githubusercontent.com/67576850/211143152-344206f4-51c3-4ab1-82ff-77baeccd5713.JPG)
![슬라이드7](https://user-images.githubusercontent.com/67576850/211143153-288abc90-96f5-4507-a8a4-b0f89b9aa5ea.JPG)
![슬라이드8](https://user-images.githubusercontent.com/67576850/211143155-702aaf21-1cfb-4f5d-a6e2-557809dd0acf.JPG)
![슬라이드9](https://user-images.githubusercontent.com/67576850/211143157-4e177cf8-504a-486e-ab81-c8f8745c7e10.JPG)
![슬라이드10](https://user-images.githubusercontent.com/67576850/211143158-5849e991-b228-4635-9c09-420c40dac06d.JPG)
