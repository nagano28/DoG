# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 17:04:42 2018

@author: Nagano Masatoshi
"""
import numpy as np
from math import exp, sqrt, pi
import matplotlib.pyplot as plt
import cv2
import copy

#DoG関数
def DoG(sig_ex, sig_in, c_ex, c_in, x):
    Gd1 = c_ex/(sig_ex*sqrt(2*pi)) * exp((x/sig_ex)**2/(-2))
    Gd2 = c_in/(sig_in*sqrt(2*pi)) * exp((x/sig_in)**2/(-2))
    w = Gd1 - Gd2
    return Gd1,Gd2,w

#グラフ描写
def plot(I_x,I,o):
    plt.figure()
    plt.plot(I_x,I)
    plt.savefig("in.png")
    plt.figure()
    plt.plot(I_x,o)
    plt.savefig("out.png")
    plt.show()
#入力I    
def IN():
    I1 = [240 for i in range(100)]
    I2 = [200 for i in range(100)]
    I3 = [160 for i in range(100)]
    I4 = [120 for i in range(100)]
    I5 = [80 for i in range(100)]
    I6 = [40 for i in range(100)]
    I = I1+I2+I3+I4+I5+I6
    I7 = np.arange(0,len(I))
#    I1w = [240 for i in range(5)]
#    I2w = [200 for i in range(5)]
#    I3w = [160 for i in range(5)]
#    I4w = [120 for i in range(5)]
#    I5w = [80 for i in range(5)]
#    I6w = [40 for i in range(5)]
#    Iw = [I1w+I2w+I3w+I4w+I5w+I6w]
#    cv2.imwrite("in2.png",Iw)
    return I,I7

def main():
    #パラメータ
    sig_ex = 1
    sig_in = 2
    c_ex = 2
    c_in = 1
    
    #Dogのx範囲
    x = np.arange(-7.5,8.0,0.2)
    Gd1 = np.zeros(len(x))
    Gd2 = np.zeros(len(x))
    w = np.zeros(len(x))
    for i in range(0,len(x)):
        Gd1[i],Gd2[i],w[i] = DoG(sig_ex, sig_in, c_ex, c_in, x[i])
    
    #入力生成
    I,I_x = IN()
    
    #wの範囲指定し、w_f生成
    w_f = np.zeros(len(x)-2*13)
    for i in range(13,len(x)-13):
        w_f[i-13] = w[i]
    
    #o(xi)=I(x)*w(x-xi)
    o = copy.deepcopy(I)
    for xx in range(26,len(I)-26):
        o_w = 0
        for xxx in range(52):
            x = xx + xxx - 26
            xi = xx - 26
            o_w += I[x]*w_f[x-xi]/sum(w_f)
        o[xx]=o_w
         
    #グラフ
    plot(I_x,I,o)
    
if __name__ == '__main__':
    main()
