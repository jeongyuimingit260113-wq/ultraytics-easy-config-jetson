# 🚀 Ultralytics Easy Config for Jetson  made by IMAI_LAB

**NVIDIA Jetson** 환경에서 복잡한 의존성 설치 과정 없이, 단 하나의 스크립트 실행만으로 **Ultralytics(YOLO 등)**를 즉시 사용할 수 있도록 최적화된 환경을 구축해 주는 프로젝트입니다.

---

## 🎯 시스템 요구 사항 (Requirements)
* **Hardware:** NVIDIA Jetson board 
* **OS:** JetPack 환경

---

## 🛠️ 주요 파일 설명
* **`ultra_jetpack.sh`**: 메인 환경 구성 및 실행 스크립트입니다. Docker 기반의 Ultralytics 환경을 자동으로 세팅하고 실행합니다.
* **`jetpack_find_run.sh`**: docker container 가 있을 경우를 대비한 예비용 스크립트 입니다.
* **`docker-compose.yml`**: pycharm IDE 인터프리터 빌드용 도커컴포즈 파일입니다. (메인 빌드용입니다)

---

## 📋 1.ultra_jetpack.sh 사용 방법 (Quick Start)

### 1. 작업 디렉토리 구성
코드를 실행하고 결과물을 저장할 메인 작업 디렉토리를 생성한 뒤, 준비된 2개의 스크립트 파일을 해당 디렉토리 안에 넣어주세요.

예시: <img width="277" height="144" alt="image" src="https://github.com/user-attachments/assets/e0c0b019-cbea-4729-996a-3264166137dd" />

```text
📦 your-project-folder
 ┣ 📜 ultra_jetpack.sh
 ┗ 📜 docker-compose.yml
```

### 2. 권한 부여 및 스크립트 실행
터미널에서 해당 디렉토리 경로로 이동한 후, 아래 명령어를 순서대로 입력하여 환경을 구축합니다.

예시: <img width="330" height="72" alt="image" src="https://github.com/user-attachments/assets/eaa31e2d-14c8-4952-b17a-ca1594d13ed9" />


#### 1. 스크립트 실행 권한 부여
````
chmod +x ultra_jetpack.sh 
````
예시: <img width="422" height="26" alt="image" src="https://github.com/user-attachments/assets/c3afc968-0d4e-4ad3-b707-49bcf94ade64" />


#### 2. 루트 권한 획득
````
sudo su
````
예시: <img width="389" height="68" alt="image" src="https://github.com/user-attachments/assets/9241b331-2cb4-4b7c-adde-6a539175c313" />


#### 3. 메인 스크립트 실행
````
./ultra_jetpack.sh
````

예시: <img width="2447" height="730" alt="image" src="https://github.com/user-attachments/assets/680a1680-0239-4991-8a3c-8c56dbf8e7a2" />

이렇게 도커 컨테이너 ID가 보이면 성공입니다.
<img width="257" height="19" alt="image" src="https://github.com/user-attachments/assets/57b8f2f2-1e1b-424e-b048-6729ee1016ef" />


#### 4. 도커 내에서 파이썬 파일 실행 방법
파이썬 파일은 무조건 같은 디렉토리내에서 실행 해주세요. (중요)
<img width="433" height="192" alt="image" src="https://github.com/user-attachments/assets/33f8cffb-f6a2-4fd7-81db-2b4f4a2c91c9" />

````
#파이썬 스크립트 예시

import torch

print(torch.cuda.is_available())

````

이렇게 뜨면 성공입니다. :<img width="445" height="33" alt="image" src="https://github.com/user-attachments/assets/ddf080ab-9dea-47d2-ad39-570d19f9a303" />

## pycharm 인터프리터 설정 ##

내 컴퓨터의 pycharm 과 jetson 보드의 SSH 설정을 이미 끝났다고 가정하고 시작합니다. 

먼저 docker에게 sudo 권한을 줍니다. 

````
sudo usermod -aG docker $USER

````


docker compose 클릭
<img width="525" height="192" alt="image" src="https://github.com/user-attachments/assets/b2df9d01-a502-4255-9f34-e523e7e5ba6a" />

구성파일의 폴더 아이콘 클릭 
<img width="373" height="368" alt="image" src="https://github.com/user-attachments/assets/248b1c6d-b86d-497d-ae99-42d0e13ff580" />

폴더에서 미리 다운 받아둔 docker-compose-yml 파일 경로를 설정합니다.
<img width="824" height="522" alt="image" src="https://github.com/user-attachments/assets/af924baf-148a-42dc-af5c-9f57b9cd4414" />

확인 클릭 
<img width="279" height="340" alt="image" src="https://github.com/user-attachments/assets/df2c1ee1-ea09-4e57-be90-b036ec93f9f2" />

다음 클릭 

<img width="359" height="356" alt="image" src="https://github.com/user-attachments/assets/a91ce1a8-d70a-41d3-acab-21a0b9948b9d" />


생성 클릭 

<img width="824" height="355" alt="image" src="https://github.com/user-attachments/assets/7d811dbd-f60e-4a86-97d9-e32fd49484af" />


그리고 좀 기다리시면 (오래 걸립니다. 인터프리터 설정)  이렇게 인터프리터 설정이 됩니다.

<img width="248" height="42" alt="image" src="https://github.com/user-attachments/assets/45badd2c-1a1f-470d-bd80-b75d269f81c2" />


아까 그 파이썬 test 코드를 실행하면 

<img width="2205" height="332" alt="image" src="https://github.com/user-attachments/assets/552facb1-bc88-48f2-be68-4b76c56946ef" />

이렇게 True 가 뜨는 걸 볼 수 있습니다. 









