# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 17:04:42 2018

@author: Nagano Masatoshi
"""
import numpy as np
from math import exp, sqrt, pi
import matplotlib.pyplot as plt

#DoG関数
def DoG(sig_ex, sig_in, c_ex, c_in, x):
    Gd1 = c_ex/(sig_ex*sqrt(2*pi)) * exp((x/sig_ex)**2/(-2))
    Gd2 = c_in/(sig_in*sqrt(2*pi)) * exp((x/sig_in)**2/(-2))
    w = Gd1 - Gd2
    return Gd1,Gd2,w

#グラフ描写
def plot(x,Gd1,Gd2,w):
    plt.plot(x,Gd1,"r",label = "Gaussian distribution 1")
    plt.plot(x,Gd2,"b",label = "Gaussian distribution 2")
    plt.plot(x,w,"g",label = "Difference of Gaussians")
    plt.legend()
    plt.xlim([-8,8]) # x軸の範囲を指定
    plt.ylim([-0.5,1]) # y軸の範囲を指定
    plt.savefig("Dog[1,2,2,1].png")
    plt.show()

def main():
    #パラメータ
    sig_ex = 1
    sig_in = 2
    c_ex = 2
    c_in = 1
    
    #xの範囲
    x = np.arange(-7.5,8.0,0.2)
    
    Gd1 = np.zeros(len(x))
    Gd2 = np.zeros(len(x))
    w = np.zeros(len(x))
    for i in range(0,len(x)):
        Gd1[i],Gd2[i],w[i] = DoG(sig_ex, sig_in, c_ex, c_in, x[i])
    plot(x,Gd1,Gd2,w)

if __name__ == '__main__':
    main()
