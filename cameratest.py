from IMVApi import *
from IMVDefines import *
import ctypes


def connect_camera():
    device = IMV_DeviceList()

    print("카메라 검색 중....")
    ret = MvCamera.IMV_EnumDevices(device, IMV_EInterfaceType.interfaceTypeAll)


    if ret != IMV_OK:
        print(f"카메라 검색 실패{ret}")
        return None
    
    print(f"카메라 검색 성공, {device.nDevNum}대의 카메라가 검색되었습니다.")



if __name__ == "__main__":
    connect_camera()
    

