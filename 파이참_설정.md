##  pycharm 인터프리터 설정 (권장 하지 않습니다!)  ##

pycharm 이 워낙 무겁기 때문에 오류가 잦아 VScode SSH를 메인으로 해주시길 바랍니다.

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
