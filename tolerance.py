import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import csv
import os
import re

x = np.arange(0.7, 1.5, 0.1) # x軸
y = np.arange(0.3, 1.1, 0.1) # y軸
X, Y = np.meshgrid(x, y)
Ro = 1.38#酸素は4配位

#pyrochloreを読み取る
Ra = []
Rb = []
path = "/mnt/c/Users/村上和則/Documents/000_reserch/pyrochlore_latticeparameter_2.csv"
with open(path) as f: 
    reader = csv.reader(f) 
    for row in csv.reader(f): 
        Ra.append(float(row[0])) 
        Rb.append(float(row[1]))


#層状ペロブスカイトを用意
#物質のリストのpath="/mnt/c/Users/村上和則/Documents/000_reserch/layer_perovskite/all.txt"
Ra_p = [1.16, 1.12, 1.26, 1.126, 1.109, 1.18, 1.26, 1.25, 1.143, 1.079, 1.066]
Rb_p = [0.605, 0.64, 0.64, 0.605, 0.605, 0.6, 0.64, 0.64, 0.605, 0.605, 0.605]

plt.subplots_adjust(wspace=0.5, hspace=0.6)


#1
plt.subplot(2,3,1)#縦横に何分割か、左上から何番目かをいれる、一桁の数字
Z1 = (3/math.sqrt(17))*((X + Ro)/(Y + Ro))
cont = plt.contourf(X,Y,Z1,cmap="rainbow", alpha=0.75, vmin=0.666,vmax=1.136)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
plt.ylabel('RB', fontsize=10)
plt.title(r"$[1] \quad t = \frac{3(R_{A} + R_{O})}{\sqrt{17}(R_{B} + R_{O})}$", fontsize=10)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.scatter(Ra_p, Rb_p, s=5, c='r', marker='o', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)


#2
plt.subplot(2,3,2)
Z2 = -(1.43373-0.42931*((X + Ro) / (Y + Ro)))
cont = plt.contourf(X,Y,Z2,cmap="rainbow", alpha=0.75, vmin=-1.040,vmax=-0.763)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
#plt.ylabel('RB', fontsize=10)
plt.title(r'$[2] \quad t = -1.4+0.4 \frac{(R_{A} + R_{O})}{(R_{B} + R_{O})}$', fontsize=10)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)




#3
plt.subplot(2,3,3)
Z3 = 0.866*((X + Ro) / (Y + Ro))
cont = plt.contourf(X,Y,Z3,cmap="rainbow", alpha=0.75, vmin=0.793,vmax=1.353)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
#plt.ylabel('RB', fontsize=10)
plt.title(r'$[3] \quad t = 0.86 \frac{(R_{A} + R_{O})}{(R_{B} + R_{O})}$', fontsize=10)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)


#4
plt.subplot(2,3,4)
x1 = 0.3125
Z4 = (math.sqrt((x1-(1/4))**2+(1/32)) / math.sqrt((x1-(1/2))**2+(1/32)))*((X + Ro)/(Y + Ro))
cont = plt.contourf(X,Y,Z4,cmap="rainbow", alpha=0.75, vmin=0.666,vmax=1.136)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
plt.ylabel('RB', fontsize=10)
plt.title(r'$[4] \quad t_{1} =  \frac{[(x-\frac{1}{4})^{2}+\frac{1}{32}]^{\frac{1}{2}}(R_{A} + R_{O})}{[(x-\frac{1}{2})^{2}+\frac{1}{32}]^{\frac{1}{2}}(R_{B} + R_{O})} $'
          "\n" r"$x=0.3125$", fontsize=8)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)


#5
plt.subplot(2,3,5)
x2 = 0.375
Z5 = (math.sqrt((x2-(1/4))**2+(1/32)) / math.sqrt((x2-(1/2))**2+(1/32)))*((X + Ro)/(Y + Ro))
cont = plt.contourf(X,Y,Z5,cmap="rainbow", alpha=0.75, vmin=0.916,vmax=1.562)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
plt.title(r'$[4] \quad t_{1} =  \frac{[(x-\frac{1}{4})^{2}+\frac{1}{32}]^{\frac{1}{2}}(R_{A} + R_{O})}{[(x-\frac{1}{2})^{2}+\frac{1}{32}]^{\frac{1}{2}}(R_{B} + R_{O})} $'
           "\n" r"$x=0.375$", fontsize=8)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)


#6
plt.subplot(2,3,6)
a=1.91712*(X + Ro) + 2.76428*(Y + Ro) + 0.04448
Z6 = -(a*(3*(3**(1/2))/8 / (X + Ro)))
cont = plt.contourf(X,Y,Z6,cmap="rainbow", alpha=0.75, vmin=-3.219,vmax=-2.405)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
#plt.ylabel('RB', fontsize=10)
plt.title(r'$[4,5] \quad t_{2} = -{a \frac{3^(\frac{3}{2})}{8(R_{A} + R_{O})}}$', fontsize=10)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)

#引用
plt.text(-1.2,0.19,"[1] Z.Song and Q.Liu, $Inorg. Chem.$, 7, 1583(2020).[2] R.Mouta et al., $Act. Cryst. Sec. B$, 69, 439(2013).", fontsize=6)
#plt.text(-1,-0.55,"[2] R.Mouta et al., $Act. Cryst. Sec. B$, 69, 439(2013).", fontsize=10)
plt.text(-1.2,0.15,"[3] V.A.Isupov, $Kristallografiya$, 3, 99(1958).[4] Cai et al., $J. Mater. Chem.$, 21, 3611(2011).", fontsize=6)
#plt.text(-1,-0.85,"[4] Cai et al., $J. Mater. Chem.$, 21, 3611(2011).", fontsize=10)
plt.text(-1.2, 0.11, "[5] M.G.Brik and A.M.Srivastava, $J.Am.Ceram.Soc$, 95, 1454(2012).", fontsize = 6)
#plt.savefig("tolerance_factor.png")
plt.show()



###



#csvファイルの整え

# csvファイルのパス
csv_file_path = "/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/chushutu_2.csv"

# csvファイルを読み込む
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # 各列の最大長を格納するリストを初期化する
    max_lengths = [0] * len(next(csv_reader))

    # 各列の最大長を求める
    for row in csv_reader:
        for i in range(len(row)):
            max_lengths[i] = max(max_lengths[i], len(row[i]))

    # csvファイルを先頭から再度読み込み、各列を空白で埋めて出力する
    csv_file.seek(0)
    output_rows = []
    for row in csv_reader:
        padded_row = []
        for i in range(len(row)):
            padded_value = row[i].ljust(max_lengths[i])
            padded_row.append(padded_value)
        output_rows.append(padded_row)

# csvファイルに出力する
output_file_path = "/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/chushutu_3.csv"
with open(output_file_path, "w", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    for row in output_rows:
        csv_writer.writerow(row)



###



#csvから組成式のみを取り出し

# csvファイルのパス
csv_file_path = os.path.join(os.path.expanduser("/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/"), "chushutu_3.csv")

# テキストファイルのパス
text_file_path = os.path.join(os.path.expanduser("/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/"), "output.txt")

# csvファイルを読み込む
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    # テキストファイルを書き込みモードで開く
    with open(text_file_path, "w") as text_file:
        for row in csv_reader:
            # 三列目の要素を取り出し、テキストファイルに書き込む
            text_file.write(row[2] + "\n")
        
###

#元素の認識

# CSVファイルの読み込み
with open('/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/chushutu_atom.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# アルファベットのみをまとめて抽出し、新たなリストに保存
output_data = []
for row in data:
    letters = ''.join([c for c in row[0] if c.isalpha()])
    output_data.append([letters])

# 新たなCSVファイルに保存
with open('/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(output_data)


###

#元素毎に取り出し

# 読み込むtxtファイル名と保存するcsvファイル名を指定
input_file = "/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_2.txt"
output_file = "/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_3.csv"

# 元素表記の正規表現パターンを定義
element_pattern = re.compile(r"[A-Z][a-z]?")

# txtファイルを読み込む
with open(input_file, "r") as f:
    lines = f.readlines()

# 新しいcsvファイルを作成してデータを書き込む
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    for line in lines:
        # 行ごとにアルファベットを抽出し、元素表記のみを抽出する
        elements = element_pattern.findall(line)
        # 新しい行に元素表記とその出現数を書き込む
        new_row = []
        for element in set(elements):
            new_row.append(element)
        writer.writerow(new_row)

###

#元素種が三種類のもののみを選ぶ

# 読み込むCSVファイル名と保存するCSVファイル名を指定
input_file = "/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_3.csv"
output_file = "/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_4.csv"


# 入力ファイルを開く
with open(input_file, 'r', newline='') as f_input:
    reader = csv.reader(f_input)
    
    # 出力ファイルを開く
    with open(output_file, 'w', newline='') as f_output:
        writer = csv.writer(f_output)
        
        # 入力ファイルから一行ずつ読み込む
        for row in reader:
            # 行の要素数が3以下の場合にのみ、行を出力ファイルに書き込む
            if len(row) <= 3:
                writer.writerow(row)

###

#１．「O」が含まれていないものは削除。２．要素が重複している行は削除。３．「O」以外の要素のみ抽出

# 入力ファイル名と出力ファイル名を指定する
input_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_4.csv'
output_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_5.csv'


# CSVファイルを読み込む
with open(input_file, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# 「O」が含まれていない行を削除する
data = [row for row in data if 'O' in row]

# 要素が完全に一致している行は一つだけ残して削除する
data = list(set(tuple(row) for row in data))

# 「O」を除いた要素のみを抽出して新しいリストを作成する
new_data = [[v for v in row if v != 'O'] for row in data]

# 新しいCSVファイルとして保存する
with open(output_file, 'w') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(new_data)                


###


#csvの元素記号とイオン半径を結びつける


# 比較対象のCSVファイルを読み込む
ref_data = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/ref_data.csv'

input_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_5.csv'
output_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_6.csv'
import csv

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
        if file2_row[0] == file1_row[0]:
            # 一致する文字列があった場合、数字を抽出して出力用のリストに追加する
            output_data.append([file2_row[0], file2_row[1], file1_row[1]])   

# 出力用のCSVファイルを作成し、出力用のリストを書き込む
with open(output_file, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(output_data)

###


#すべてのイオン半径を抽出
#output_8がイオン半径抽出できたもの、[2,4]列が数字

import csv
ref_data = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/ref_data.csv'
input_2_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_6.csv'
output_2_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_7.csv'
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
        if file4_row[0] == file3_row[2]:
            # 一致する文字列があった場合、数字を抽出して出力用のリストに追加する
            output_2_data.append([file3_row[0], file3_row[1], file3_row[2], file4_row[1]])   

# 出力用のCSVファイルを作成し、出力用のリストを書き込む
with open(output_2_file, 'w', newline='') as output_2_file:
    writer = csv.writer(output_2_file)
    writer.writerows(output_2_data)


###

#イオン半径のcsvを、イオン半径の大きなモノ（Aさいと）を第四列に、イオン半径の小さなもの（Bさいと）を第二列に入れる

input_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_7.csv'
output_file = '/mnt/c/Users/村上和則/Documents/000_reserch/exp_inorg_chu/output_8.csv'
# CSVファイルを読み込む
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader) # ヘッダー行をスキップする
    rows = []
    for row in csvreader:
        # 第2列と第4列を比較して、入れ替えが必要ならば行を修正する
        if float(row[1]) > float(row[3]):
            row[1], row[3] = row[3], row[1]
            row[0], row[2] = row[2], row[0]
        rows.append(row)

# 結果をCSVファイルに書き込む
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)

###

#この最後のpathをプロットするpathに指定すれば図にプロットできる