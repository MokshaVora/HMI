from tkinter import *
import Gyroscope
import EMG
import subprocess

window = Tk()

window.title('Human Machine Interface')

flag_button1 = 0
flag_button2 = 0

process1 = None
process2 = None
process3 = None
process4 = None

def click_button1():
    global flag_button1,process1,process2
    print('button 1 click')
    button1.configure(state='normal')
    
    if flag_button1 % 2 == 0:
        flag_button1 = 1
        process1 = subprocess.Popen(["python", "Gyroscope.py",'1'])
        process2 = subprocess.Popen(["python", "EMG.py",'1'])
    else:
        flag_button1 = 0
        process1.terminate()
        process2.terminate()

def click_button2():
    global flag_button2,process3,process4
    print('button 2 click')
    button2.configure(state='normal')
    
    if flag_button2 % 2 == 0:
        flag_button2 = 1
        process3 = subprocess.Popen(["python", "Gyroscope.py",'2'])
        process4 = subprocess.Popen(["python", "EMG.py",'2'])
    else:
        flag_button2 = 0
        process3.terminate()
        process4.terminate()

def click_button3():
    print('button 3 click')

button1 = Button(window, text = 'Button1', height = 5, width = 50, command = click_button1)
button1.grid(column = 0 , row = 0)

button2 = Button(window, text = 'Button2', height = 5, width = 50, command = click_button2)
button2.grid(column = 0 , row = 10)

button3 = Button(window, text = 'Button3', height = 5, width = 50, command = click_button3)
button3.grid(column = 0 , row = 20)

window.mainloop()
