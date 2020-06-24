#!/usr/bin/python3

import serial
import signal # Ctrl-C -> quit

signal.signal(signal.SIGINT, signal.SIG_DFL)
ser = serial.Serial('/dev/ttyUSB0', 115200)

ser.write(b'sgi\n')                     #送りたい内容をバイト列で送信
print(ser.readline())                   #行終端'¥n'までリードする
ser.write(b'sgb,36,0xabcd,100,20\n')
print(ser.readline())

ser.close()

#シリアル通信(PC⇔Arduino)
#ser = serial.Serial()
#ser.port = "COM4"     #デバイスマネージャでArduinoのポート確認
#ser.baudrate = 115200 #Arduinoと合わせる
#ser.setDTR(False)     #DTRを常にLOWにしReset阻止
#ser.open()            #COMポートを開く
#ser.write(b'1')       #送りたい内容をバイト列で送信
#ser.close()           #COMポートを閉じる

