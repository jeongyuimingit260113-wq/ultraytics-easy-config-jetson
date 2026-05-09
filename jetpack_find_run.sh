#!/bin/bash 

echo "nvidia jetpack 버전을 먼저 확인 하겠습니다."

JETPACK_VER=$(apt show nvidia-jetpack 2>/dev/null | grep -i "Version:" | awk '{print $2}' | awk -F. '{print $1}')

if [ -z "$JETPACK_VER" ]; then
  echo "jetpack 설치를 확인 할 수 없습니다."

else
  echo "현재 설치된 jetpack 버전은 ${JETPACK_VER} 임으로 현재 버전으로 설치 하겠습니다. "

fi

INSTALL_NAME="latest-jetson-jetpack${JETPACK_VER}"

T_UP=ultralytics/ultralytics:$INSTALL_NAME


sudo docker pull "${T_UP}"

PWD=$(pwd)


sudo docker run -it --rm --ipc=host --runtime=nvidia --gpus all -v "${PWD}":/usr_creative -w /usr_creative "${T_UP}"

