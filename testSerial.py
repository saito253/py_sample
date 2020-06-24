#!/usr/bin/python3

import serial

# Ctrl-C でexit
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# timeoutを秒で設定（default:None)ボーレートはデフォルトで9600
#ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)
ser = serial.Serial('/dev/ttyUSB0', 115200)
#for i in range(1,100):
while 1:
#    c = ser.read()      # 1文字読み込み
#    str = ser.read(10)  # 指定も字数読み込み ただしtimeoutが設定されている婆は読み取れた分だけ
    line = ser.readline()  # 行終端'¥n'までリードする
    print(line)

ser.close()

#シリアル通信(PC⇔Arduino)
#ser = serial.Serial()
#ser.port = "COM4"     #デバイスマネージャでArduinoのポート確認
#ser.baudrate = 115200 #Arduinoと合わせる
#ser.setDTR(False)     #DTRを常にLOWにしReset阻止
#ser.open()            #COMポートを開く
#ser.write(b'1')       #送りたい内容をバイト列で送信
#ser.close()           #COMポートを閉じる

