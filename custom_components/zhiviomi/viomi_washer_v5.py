from enum import IntEnum
#http://miot-spec.org/miot-spec-v2/instance?type=urn:miot-spec-v2:device:washer:0000A01F:viomi-v5:1

SRV_Device_Information = 1
PROP_Device_Manufacturer = 1
PROP_Device_Model = 2
PROP_Device_Serial_Number = 3
PROP_Current_Firmware_Version = 4

SRV_Washer = 2
PROP_Switch_Status = 1 #bool #rwn
PROP_Status = 2 #uint8 #rn
class VALUE_Status(IntEnum):
    Idle = 1
    Busy = 2
    Fault = 3
    Off = 4
PROP_Mode = 3 #uint8 #rw
class VALUE_Mode(IntEnum):
    Gold_Dry = 1
    Weak_Dry = 2
    Refresh = 3
    Gold_Wash = 4
    Super_Quick = 5
    Cotton = 6
    Wool = 7
    Down_Coat = 8
    Drum_Clean = 9
    Bactericidal_Wash = 10
    Rinse_Spin = 11
    Spin = 12
    Quick_Wash = 13
    Shirt = 14
    Jeans = 15
    Underwear = 16
PROP_Left_Time = 4 #uint32
class VALUE_Left_Time(IntEnum):
    MIN = 0
    MAX = 65535
PROP_Target_Temperature = 5 #float #rw
class VALUE_Target_Temperature(IntEnum):
    MIN = 0
    MAX = 100
PROP_Spin_Speed = 6 #uint16 #rw
class VALUE_Spin_Speed(IntEnum):
    MIN = 0
    MAX = 1300
ACTION_Start_Wash = 1
ACTION_Pause = 2
ACTION_Stop_Washing = 3

SRV_Physical_Control_Locked = 3
PROP_Physical_Control_Locked = 1 #bool #rw


