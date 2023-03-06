#E_hull毎にプロット

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import csv
import os
import sys




#csvの元素記号とイオン半径を結びつける


# 比較対象のCSVファイルを読み込む
ref_data = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/ref_data.csv'

input_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output.csv'
output_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output_1.csv'

# 1つ目のCSVファイルを読み込む
with open(input_file, 'r') as file1:
    reader1 = csv.reader(file1)
    file1_data = list(reader1)

# 2つ目のCSVファイルを読み込む
with open(ref_data, 'r') as file2:
    reader2 = csv.reader(file2)
    file2_data = list(reader2)

# 出力用のリストを初期化
output_data = []

# 2つ目のCSVファイルの各行について、1つ目のCSVファイルの各行と一致する文字列があるかを調べる
for file2_row in file2_data:
    for file1_row in file1_data:
        if file2_row[0] == file1_row[1]:
            # 一致する文字列があった場合、数字を抽出して出力用のリストに追加する
            output_data.append([file1_row[0], file1_row[1], file2_row[1],file1_row[2]])   

# 出力用のCSVファイルを作成し、出力用のリストを書き込む
with open(output_file, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(output_data)


input_2_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output_1.csv'
output_2_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output_2.csv'
# 1つ目のCSVファイルを読み込む
with open(input_2_file, 'r') as file1:
    reader1 = csv.reader(file1)
    file3_data = list(reader1)

# 2つ目のCSVファイルを読み込む
with open(ref_data, 'r') as file2:
    reader2 = csv.reader(file2)
    file4_data = list(reader2)

# 出力用のリストを初期化
output_2_data = []

# 2つ目のCSVファイルの各行について、1つ目のCSVファイルの各行と一致する文字列があるかを調べる
for file4_row in file4_data:
    for file3_row in file3_data:
        if file4_row[0] == file3_row[3]:
            # 一致する文字列があった場合、数字を抽出して出力用のリストに追加する
            output_2_data.append([file3_row[0], file3_row[1], file3_row[2], file3_row[3], file4_row[1]])   

# 出力用のCSVファイルを作成し、出力用のリストを書き込む
with open(output_2_file, 'w', newline='') as output_2_file:
    writer = csv.writer(output_2_file)
    writer.writerows(output_2_data)







#pyroshloreの物質を、形成エネルギーの小さい順に並べ変える

input_3_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output_2.csv'
output_3_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output_3.csv'


# CSVファイルからデータを読み込む
with open(input_3_file ) as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# 第1列をfloat型に変換して並べ替える
sorted_data = sorted(data[0:], key=lambda x: float(x[0]))

# ソートされたデータをCSVファイルに書き込む
with open(output_3_file , 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data[0])
    writer.writerows(sorted_data)





#イオン半径のcsvを、イオン半径の大きなモノ（Aさいと）を第四列に、イオン半径の小さなもの（Bさいと）を第二列に入れる

input_4_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output_3.csv'
output_4_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output_4.csv'
# CSVファイルを読み込む
with open(input_4_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader) # ヘッダー行をスキップする
    rows = []
    for row in csvreader:
        # 第2列と第4列を比較して、入れ替えが必要ならば行を修正する
        if float(row[4]) > float(row[2]):
            row[1], row[3] = row[3], row[1]
            row[2], row[4] = row[4], row[2]
        rows.append(row)

# 結果をCSVファイルに書き込む
with open(output_4_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)










input_5_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output_4.csv'
output_5_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/pyrochlore_Ehull_output_5.gif'


# CSVファイルからデータを読み込む
with open(input_5_file) as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# 最初のnum_rows行のデータを取得する
num_rows = 15 # 上から100行までを取得する例
x_data = [float(row[2]) for row in data[1:num_rows]]
y_data = [float(row[4]) for row in data[1:num_rows]]

# 散布図をプロットする
plt.scatter(x_data, y_data, s=30, c='k', marker='+', alpha=0.75)

# プロットを表示する
plt.savefig("test_chatgpt_Ehull.png")





x = np.arange(0.34, 1.56, 0.1) # x軸
y = np.arange(0.34, 1.56, 0.1) # y軸
X, Y = np.meshgrid(x, y)
Ro = 1.38#酸素は4配位


#pyrochloreを読み取り配列に
Ra = []
Rb = []
path = "/mnt/c/Users/村上和則/Documents/000_reserch/pyrochlore_latticeparameter_2.csv"
with open(path) as f: 
    reader = csv.reader(f) 
    for row in csv.reader(f): 
        Ra.append(float(row[0])) 
        Rb.append(float(row[1]))


#fig, ax = plt.subplots_adjust(wspace=0.5, hspace=0.6)
fig, ax = plt.subplots()


#層状ペロブスカイトを用意
#物質のリストのpath="/mnt/c/Users/村上和則/Documents/000_reserch/layer_perovskite/all.txt"
Ra_p = [1.16, 1.12, 1.26, 1.126, 1.109, 1.18, 1.26, 1.25, 1.18]
Rb_p = [0.605, 0.64, 0.64, 0.605, 0.605, 0.6, 0.64, 0.64, 0.59]




#1
#plt.subplot(2,3,1)#縦横に何分割か、左上から何番目かをいれる、一桁の数字
Z1 = (3/math.sqrt(17))*((X + Ro)/(Y + Ro))
cont = plt.contourf(X,Y,Z1,cmap="rainbow", alpha=0.75, vmin=0.45,vmax=1.15)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
plt.ylabel('RB', fontsize=10)
plt.title(r"$[1] \quad t = \frac{3(R_{A} + R_{O})}{\sqrt{17}(R_{B} + R_{O})}$", fontsize=10)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=50, c='r', marker='+', alpha=0.75)
plt.scatter(Ra_p, Rb_p, s=50, c='b', marker='^', alpha=0.75)
plt.xlim(0.35, 1.55)
plt.ylim(0.35, 1.55)
###

# CSVファイルからデータを読み込む
df = pd.read_csv(input_5_file)

# 第3列と第5列の値を取得する
x = df.iloc[:, 2].values
y = df.iloc[:, 4].values

# プロットの色を設定する
n = len(x)  # データ数
cmap = plt.get_cmap('gray')  # カラーマップを取得する
colors = cmap(np.linspace(0, 1, n))  # カラーマップをデータ数分だけ等間隔に分割する

# 散布図をプロットする
for i in range(n):
    ax.plot(x[i], y[i], 'o', color=colors[i], markersize=5)


import matplotlib.ticker as ticker

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=n-1))
sm.set_array([])

# カラーバーの目盛りの値を文字列で指定
cbar_ticks = [0, 11, 22, 32, 53, 75]
cbar_ticklabels = ['0', '0.01', '0.05', '0.1', '0.2', '0.55']

# カラーバーを追加
cbar = plt.colorbar(sm, ticks=cbar_ticks, format=ticker.FixedFormatter(cbar_ticklabels))
cbar.set_label('Energy above Convex Hull (eV)')

plt.savefig("test_chatgpt_Ehull_2.png")
