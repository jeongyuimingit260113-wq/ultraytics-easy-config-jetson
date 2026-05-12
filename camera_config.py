from IMVApi import *
from IMVDefines import *
import ctypes 
import numpy as np 
import time
def connect_camera():
    device = IMV_DeviceList()

    print("카메라 검색 중....")
    ret = MvCamera.IMV_EnumDevices(device, IMV_EInterfaceType.interfaceTypeAll)


    if ret != IMV_OK:
        print(f"카메라 검색 실패{ret}")
        return None
    
    print(f"카메라 검색 성공, {device.nDevNum}대의 카메라가 검색되었습니다.")

    dev_info = device.pDevInfo[0]

    camera_name = dev_info.cameraName.decode('ascii').rstrip('\x00')
    print(f"카메라 이름: {camera_name}")

    serial_number = dev_info.serialNumber.decode('ascii').rstrip('\x00')
    print(f"시리얼 번호: {serial_number}")


    if dev_info.nCameraType == IMV_ECameraType.typeGigeCamera:

        ip_address = dev_info.DeviceSpecificInfo.gigeDeviceInfo.ipAddress.decode('ascii').rstrip('\x00') 
        

    else:
        print("카메라 유형이 GigE 카메라가 아닙니다.")

    return ip_address


def handle_camera(ip_address):
   
    p_ip = ctypes.cast(ctypes.c_char_p(ip_address.encode('ascii')), ctypes.c_void_p)

    ret = cam.IMV_CreateHandle(IMV_ECreateHandleMode.modeByIPAddress, p_ip)

    ret = cam.IMV_Open()
    if ret != IMV_OK:
        print(f"카메라 핸들 생성 실패: {ret}")
        return None
    
    ret = cam.IMV_StartGrabbing()
    if ret != IMV_OK:
        print(f"카메라 영상 수집 시작 실패: {ret}")
        cam.IMV_Close()
        cam.IMV_DestroyHandle()
        return 
    
    print("스트리밍 시작! 종료 press p")

    try:
        while True: 
            frame = IMV_Frame()
            ret = cam.IMV_GetFrame(frame, 500)
            if ret == IMV_OK:
                raw_data = ctypes.string_at(frame.pData, frame.frameInfo.size)

                img = np.frombuffer(raw_data, dtype=np.uint8).reshape(
                    (frame.frameInfo.height, frame.frameInfo.width)
                )

                cam.IMV_ReleaseFrame(frame)
                yield img # 처리부로 데이터 전달
            else:
                time.sleep(0.01) # CPU 과부하 방지

    finally: 
        
        cam.IMV_StopGrabbing()
        cam.IMV_Close()
        cam.IMV_DestroyHandle()
        print("스트리밍 종료!")




            


if __name__ == "__main__":
    cam = MvCamera()
    ip = connect_camera()
    for img in handle_camera(ip):
        print(f"받은 이미지 크기: {img.shape}")






