# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 17:04:42 2018

@author: Nagano Masatoshi
"""
import numpy as np
import math
from math import exp, sqrt
import matplotlib.pyplot as plt

#DoGフィルタのマスク
def DoG(sig_ex, sig_in, c_ex, c_in, x):
    a = c_ex/(sig_ex * sqrt(2 * math.pi))
    b = exp((x/sig_ex)**2/(-2))
    c = c_in/(sig_in * sqrt(2 * math.pi))
    d = exp((x/sig_in)**2/(-2))
    G1 = a * b
    G2 = c * d
    w = G1 - G2
    return w

#グラフ描写
def plot(w):
    plt.plot(w, "-", color = "k", markerfacecolor = "k",marker = ".")
    plt.xlim([0,149]) # x軸の範囲を 0 <= x <= 149 に
    plt.ylim([80,200]) # y軸の範囲を 80 <= y <= 200 に
    plt.show()

def main():
    #変数に代入
    sig_ex = 1
    sig_in = 2
    c_ex = 1.5
    c_in = 1

    #xを離散化
    x = np.arange(-7.5,8.0,0.5)

    #入力信号Iを定義                   ...問2-(イ)
    I1 = [[175] for i in range(30)]
    I2 = [[157] for i in range(30)]
    I3 = [[140] for i in range(30)]
    I4 = [[121] for i in range(30)]
    I5 = [[109] for i in range(30)]
    I6 = [[97] for i in range(30)]
    I = np.r_[I1,I2,I3,I4,I5,I6]

    #DoGフィルタのマスク生成
    w = np.zeros(31)
    for i in range(0, 31):
        w[i] = DoG(sig_ex, sig_in, c_ex, c_in, x[i])

    #DoGフィルタ処理
    g = np.zeros(150)
    for j in range(0, 150):
        for k in range(0, 31):
            g[j] += w[k]*I[j+k]

    #グラフ描写
    plot(g)

if __name__ == '__main__':
    main()
