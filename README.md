# 🚀 Ultralytics Easy Config for Jetson  made by IMAI_LAB

**NVIDIA Jetson** 환경에서 복잡한 의존성 설치 과정 없이, 단 하나의 스크립트 실행만으로 **Ultralytics(YOLO 등)**를 즉시 사용할 수 있도록 최적화된 환경을 구축해 주는 프로젝트입니다.

---

## 🎯 시스템 요구 사항 (Requirements)
* **Hardware:** NVIDIA Jetson board 
* **OS:** JetPack 환경
* **huarry-vision-cam-sdk** (저작권 이슈 때문에 올리지 못했습니다.)

---

## 🛠️ 주요 파일 설명
* **`ultra_jetpack.sh`**: 메인 환경 구성 및 실행 스크립트입니다. Docker 기반의 Ultralytics 환경을 자동으로 세팅하고 실행합니다.
* **`jetpack_find_run.sh`**: docker container 가 있을 경우를 대비한 예비용 스크립트 입니다.
* **`docker-compose.yml`**: 메인빌드용 docker compose 파일입니다. (메인 빌드용입니다)
* **`settings.json`**: vscode 인터프리터 설정용 파일입니다.

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

아래는 github 파이썬 예시 결과 입니다. <img width="512" height="165" alt="image" src="https://github.com/user-attachments/assets/bca44820-848d-4c8f-885a-452e866158bb" />



## 3. 그 외 기타  ## 

만약 실행중인 docker을 보고 싶다면

````
docker ps

````

실행을 멈추고 싶다면 

````
docker stop  #docker name

````









