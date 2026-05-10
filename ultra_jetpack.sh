#!/bin/bash


echo "container 설치 저장소 인식 과정을 거치겠습니다."

curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
  | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
    | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update

echo "container 툴을 설치 합니다. "

sudo apt-get install -y nvidia-container-toolkit \
  nvidia-container-toolkit-base libnvidia-container-tools \
  libnvidia-container1

echo "container 설정 중..."

sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker


echo "nvidia jetpack 버전을 먼저 확인 하겠습니다."

JETPACK_VER=$(apt show nvidia-jetpack 2>/dev/null | grep -i "Version:" | awk '{print $2}' | awk -F. '{print $1}')

if [ -z "$JETPACK_VER" ]; then
  echo "jetpack 설치를 확인 할 수 없습니다."

else
  echo "현재 설치된 jetpack 버전은 ${JETPACK_VER} 임으로 6버전으로 설치 하겠습니다. "

fi

INSTALL_NAME="latest-jetson-jetpack${JETPACK_VER}"

T_UP=ultralytics/ultralytics:$INSTALL_NAME
echo "T_UP=${T_UP}" > .env


sudo docker compose run --rm IMAI-LAB


