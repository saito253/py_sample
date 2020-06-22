#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dat = []
with open('/home/saito/data/mlx.csv', 'r') as f:
    for line in f:
#       print(line[7:11])
        dat.append(float(line[7:11]))

#df = pd.read_csv('/home/saito/data/mlx.csv', index_col=1)
#print(df)

#dat = [40, 31.2, 35.2, 33.5]

print("max: ",np.max(dat))
print("min: ",np.min(dat))
print("ave: ",np.average(dat))
print("std: ",np.std(dat))
'''

# 平均10、標準偏差10 の正規乱数を100件生成
x = np.random.normal(ave, std, 1000)

print(x)
'''

plt.hist(dat)
# ヒストグラムを表示
plt.show()
# 引数にbins=数字でヒストグラムの棒の数を指定できます。
# plt.hist(x, bins=16)
# orientation="horizontal"を指定することで横棒として描画も可能です。

'''
############ sample program 3 (棒グラフ) ###########
import matplotlib.pyplot as plt
a = range(0, 7)
b = [55,21,61,98,85,52,99]
plt.bar(a, b)
# plt.barh(a, b) # 横棒の棒グラフ
plt.show()
 
import matplotlib.pyplot as plt
import numpy as np
 
# 棒グラフ
m = ("33.2", "33.3", "33.4", "33.5", "33.6", "33.7", "7","8","9","10","11","12")
y_pos = np.arange(len(m))
# 下記sales変数内の数値を変更して、色々実行してみてください。
sales = [10 ,18 ,32,54,65,96, 120, 140, 145,162, 188, 202]
 
plt.bar(y_pos, sales, alpha=0.5)
plt.ylabel("Usage")
plt.title("Sales Trends") # 売上推移
plt.show()
'''

'''
############ sample program 2(曲線グラフ) ###########

import numpy as np
import matplotlib.pyplot as plt
 
x = np.arange(-5, 5, 0.1) #-5から5まで0.1区切りで配列を作る
y = np.sin(x) #配列xの値に関してそれぞれsin(x)を求めてy軸の配列を生成
 
plt.plot(x,y) # この場合のplot関数の第一引数xは、x軸に対応し、第二引数のyがy軸にあたります。
plt.show()
'''

'''
############ sample program 1 ###########
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
 
# クラスA、Bの生徒の身長
A=[165,168,171,177,171,162,163,166,168,187,172,177]
B=[188,161,174,155,184,187,160,158,178,175,160,165]
 
# 標準偏差を算出
np.std(A) # 6.77...
np.std(B) # 11.49...
'''
