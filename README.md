# 🚀 Ultralytics Easy Config for Jetson

**NVIDIA Jetson Orin NX (JetPack 6)** 환경에서 복잡한 의존성 설치 과정 없이, 단 하나의 스크립트 실행만으로 **Ultralytics(YOLO 등)**를 즉시 사용할 수 있도록 최적화된 환경을 구축해 주는 프로젝트입니다.

---

## 🎯 시스템 요구 사항 (Requirements)
* **Hardware:** NVIDIA Jetson Orin NX (최적화 타겟)
* **OS:** JetPack 6.x 환경

---

## 🛠️ 주요 파일 설명
* **`ultra_jetpack.sh`**: 메인 환경 구성 및 실행 스크립트입니다. Docker 기반의 Ultralytics 환경을 자동으로 세팅하고 실행합니다.
* **`jetpack_find_run.sh`**: 기존에 생성된 Docker 컨테이너가 중지(`docker stop`)되었거나 기기 재부팅 후, 기존 작업 환경을 다시 불러와 실행할 때 사용하는 복구용 스크립트입니다.

---

## 📋 사용 방법 (Quick Start)

### 1. 작업 디렉토리 구성
코드를 실행하고 결과물을 저장할 메인 작업 디렉토리를 생성한 뒤, 준비된 2개의 스크립트 파일을 해당 디렉토리 안에 넣어주세요.

```text
📦 your-project-folder
 ┣ 📜 ultra_jetpack.sh
 ┗ 📜 jetpack_find_run.sh
```


## 2. 권한 부여 및 스크립트 실행
터미널에서 해당 디렉토리 경로로 이동한 후, 아래 명령어를 순서대로 입력하여 환경을 구축합니다.

Bash
# 1. 스크립트 실행 권한 부여
````
chmod +x ultra_jetpack.sh jetpack_find_run.sh
````

# 2. 루트 권한 획득
````
sudo su
````

# 3. 메인 스크립트 실행
````
./ultra_jetpack.sh
````

---
## 3. 도커 close 방법 
````
docker stop
````
이미 rm 명령어 활성으로 인해 stop을 한 경우 모든 도커 파일이 날라갑니다. 
