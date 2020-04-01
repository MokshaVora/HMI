import re
import sys
import serial
import traceback
import pyautogui as pyg
import serial.tools.list_ports
from codecs import decode
from Keyboard import *

pyg.PAUSE = 0

threshold = 240

action = ''

def connect(): 
    connected = []
    while 'COM5' not in connected:
        comlist = serial.tools.list_ports.comports()
        connected = []
        for element in comlist:
            connected.append(element.device)
        print('EMG not connected')
    print('EMG connected')
    return 1

def main(n=1):
    ser = serial.Serial('COM5',9600)
    while True:
        try:
            data = ser.readline()[:-2].decode()
            emg = [int(d) for d in re.findall(r'-?\d+',data)]

            if emg > threshold:
                if n == 1:
                    pyautogui.click(clicks=2)
                    print('emg double click')
                if n == 2:
                    ReleaseKey(A)
                    ReleaseKey(S)
                    ReleaseKey(D)
                    PressKey(X)
                    print('emg x-boost')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#                 
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            if n == 2:
                ReleaseKey(W)
                ReleaseKey(A)
                ReleaseKey(S)
                ReleaseKey(D)
            break
        except serial.serialutil.SerialException:
            print('EMG Disconnect')
            if connect() == 1:
                ser = serial.Serial('COM5',9600)
        except Exception:
            traceback.print_exc()
            print('Error')

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
    except:
        n = 1
    if connect() == 1:
        main(n)
