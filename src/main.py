import camera_config
from IMVApi import *
import cv2
import zmq
from  ultralytics import YOLO 

model = YOLO("yolo26n.engine")

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

print("✅ ZMQ 서버 대기 중... 카메라를 연결합니다.")

# 2. 카메라 영상 받아오기 루프
for i in camera_config.handle_camera(camera_config.connect_camera(), MvCamera()):

    img = cv2.cvtColor(i, cv2.COLOR_GRAY2RGB)

    results = model.track(img, persist=True, imgsz=320 , conf=0.2)
    annotated_frame = results[0].plot()
    
    # 3. 이미지를 JPEG로 압축 (품질 80: 속도와 화질의 적절한 타협점)
    success, encoded_img = cv2.imencode('.jpg', annotated_frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
    
    if success:
        # 4. 바이트 형태로 변환하여 전송
        socket.send(encoded_img.tobytes())

print("스트리밍 종료")

