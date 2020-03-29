import re
import sys
import serial
import traceback
import pyautogui as pyg
import serial.tools.list_ports
from codecs import decode
from Keyboard import *

pyg.PAUSE = 0

min_xy = 10
max_xy = 60

action = ''

def connect(): 
    connected = []
    while 'COM3' not in connected:
        comlist = serial.tools.list_ports.comports()
        connected = []
        for element in comlist:
            connected.append(element.device)
        print('Gyroscope not connected')
    print('Gyroscope connected')
    return 1

def distance(data):
    d = [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
             2, 2, 2, 3, 3, 3, 4, 4, 4, 4,
             5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
             6, 7, 8, 8, 9, 9,10,10,11,12,
            12,12,13,13,13,14,14,14,15,15,
            16,16,17,17,18,18,19,19,20,20]
    
    return d[abs(data)]

def main(n=1):
    ser = serial.Serial('COM3',9600)
    while True:
        try:
            data = ser.readline()[:-2].decode()
            gyro_x , gyro_y = [int(d) for d in re.findall(r'-?\d+',data)]

            if abs(gyro_x) < min_xy or abs(gyro_x) > max_xy:
                gyro_x = 0
            if abs(gyro_y) < min_xy or abs(gyro_y) > max_xy:
                gyro_y = 0

            gyro_sum = gyro_x + gyro_y
            gyro_diff = gyro_x - gyro_y
           
            if gyro_x == 0 and gyro_y == 0:
                if n == 1:
                    action = 'same'
                    print('(gyro_x : {}, gyro_y : {}) (action : {})'.format(gyro_x,gyro_y,action))
                if n == 2:
                    ReleaseKey(S)
                    ReleaseKey(A)
                    ReleaseKey(D)
                    PressKey(W)
                    print('same')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
            elif gyro_sum >= 0 and gyro_diff <= 0:
                if n == 1:
                    curser_x, curser_y = pyg.position()
                    curser_distance = distance(gyro_y)                  
                    if pyg.onScreen(curser_x - curser_distance , curser_y):
                        action = 'left'
                        pyg.moveTo(curser_x - curser_distance , curser_y , duration = 0)
                    else:
                        action = 'left nai thay'
                    print('(gyro_x : {}, gyro_y : {}) (action : {}) {}'.format(gyro_x,gyro_y,action,curser_distance))
                if n == 2:
                    ReleaseKey(S)
                    ReleaseKey(D)
                    PressKey(W)
                    PressKey(A)
                    print('a-left')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
            elif gyro_sum <= 0 and gyro_diff >=0:
                if n == 1:
                    curser_x, curser_y = pyg.position()
                    curser_distance = distance(gyro_y)
                    if pyg.onScreen(curser_x + curser_distance , curser_y):
                        action = 'right'	
                        pyg.moveTo(curser_x + curser_distance , curser_y , duration = 0)
                    else:
                        action = 'right nai thay'
                    print('(gyro_x : {}, gyro_y : {}) (action : {}) {}'.format(gyro_x,gyro_y,action,curser_distance))
                if n == 2:
                    ReleaseKey(A)
                    ReleaseKey(S)
                    PressKey(W)
                    PressKey(D)
                    print('d-ringt')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#                   
            elif gyro_sum > 0 and gyro_diff > 0:
                if n == 1:
                    curser_x, curser_y = pyg.position()
                    curser_distance = distance(gyro_x)
                    if pyg.onScreen(curser_x , curser_y - curser_distance):	
                        action = 'up'		
                        pyg.moveTo(curser_x , curser_y - curser_distance , duration = 0)
                    else:
                        action =  'up nai thay'
                    print('(gyro_x : {}, gyro_y : {}) (action : {}) {}'.format(gyro_x,gyro_y,action,curser_distance))
                if n == 2:
                    ReleaseKey(S)
                    ReleaseKey(A)
                    ReleaseKey(D)
                    PressKey(W)
                    print('w-up')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
            elif gyro_sum < 0 and gyro_diff < 0:
                if n == 1:
                    curser_x, curser_y = pyg.position()
                    curser_distance = distance(gyro_x)
                    if pyg.onScreen(curser_x , curser_y + curser_distance):
                        action = 'down'	
                        pyg.moveTo(curser_x , curser_y + curser_distance ,duration = 0)	
                    else:
                        action = 'down nai thay'
                    print('(gyro_x : {}, gyro_y : {}) (action : {}) {}'.format(gyro_x,gyro_y,action,curser_distance))
                if n == 2:
                    ReleaseKey(W)
                    ReleaseKey(A)
                    ReleaseKey(D)
                    PressKey(S)
                    print('s-down')
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
            print('Gyroscope Disconnect')
            if connect() == 1:
                ser = serial.Serial('COM3',9600)
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
