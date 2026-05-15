##  vscode 인터프리터 설정 (권장)  ##

SSH 설정을 이미 안다고 가정하고 이미 스크립트로 업데이트가 끝났고 도커 를 종료한 상태라고 가정하고 시작합니다. 



###  sudo 권한을 가지고 시작 ### 
````
sudo su

````
예시 : <img width="202" height="80" alt="화면 캡처 2026-05-12 151812 - 복사본 (2)" src="https://github.com/user-attachments/assets/c2813caf-ff5f-4208-a1cd-f8f45d683102" />




### 해당 디렉토리 이동 후 docker 빌드 ### 
````
docker compose up
````

예시: <img width="603" height="122" alt="image" src="https://github.com/user-attachments/assets/79b22f44-f342-4de6-b646-b49c3bc26dd3" />

### 도커 이동 후 zmq 설치 ###

````
pip install zmq

````


### docker 권한 설정 ###

````

sudo usermod -aG docker $USER

````

만약 도커를 내리고 싶다면 

````
docker compose down
````

예시: <img width="636" height="87" alt="image" src="https://github.com/user-attachments/assets/db50e1bc-8a79-4085-99d5-a304a9720078" />



### SSH 연결 아이콘 누르고 dev container 로 이동 ###
<img width="320" height="380" alt="image" src="https://github.com/user-attachments/assets/9c957327-50a0-4134-876e-afe112b6b686" />



### attach-window +창 아이콘 클릭 ###
<img width="324" height="60" alt="image" src="https://github.com/user-attachments/assets/bd5e0eca-b0ca-4386-a82d-5724bfc04f0a" />



### 들어와서 settings.json 을 github의 setting.json으로 대체 ### 

<img width="303" height="67" alt="image" src="https://github.com/user-attachments/assets/93e304c3-6fb5-4161-8769-942bb4fab408" />


