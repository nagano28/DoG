# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 17:04:42 2018

@author: Nagano Masatoshi
"""
import numpy as np
from math import exp, sqrt, pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
import copy
#DoG関数
def DoG(sig_ex, sig_in, c_ex, c_in, x, y):
    Gd1 = c_ex/(sig_ex*sqrt(2*pi)) * exp((((x**2)+(y**2))/sig_ex**2)/(-2))
    Gd2 = c_in/(sig_in*sqrt(2*pi)) * exp((((x**2)+(y**2))/sig_in**2)/(-2))
    w = Gd1 - Gd2
    return Gd1,Gd2,w

#グラフ描写
def plot(x,y,Gd1,Gd2,w):
    X,Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('w')
    #ax.plot_wireframe(X, Y, Gd1, color="r")
    #ax.plot_wireframe(X, Y, Gd2, color="b")
    ax.plot_wireframe(X, Y, w, color="g")
    plt.savefig("Dogxy_w.png")
    plt.show()

def IN():
    I = np.zeros((600,600))
    for j in range(300):
        for i in range(300):
            I[j][i] = 230
        for i in range(300,600):
            I[j][i] = 100
    for j in range(300,600):
        for i in range(300):
            I[j][i] = 100
        for i in range(300,600):
            I[j][i] = 230
    return I
    
def main():
    #パラメータ
    sig_ex = 1
    sig_in = 2
    c_ex = 2
    c_in = 1
    
    #x,yの範囲
    #I = np.zeros((600,600))
    x = np.arange(-7.5,8.0,0.2)
    y = np.arange(-7.5,8.0,0.2)
    Gd1 = np.zeros((len(y),len(x)))
    Gd2 = np.zeros((len(y),len(x)))
    w = np.zeros((len(y),len(x)))
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            Gd1[j][i],Gd2[j][i],w[j][i] = DoG(sig_ex, sig_in, c_ex, c_in, x[i], y[j])
    I = IN()
    np.savetxt('In.txt',I)
    
    w_f = np.zeros((len(y)-2*13,len(x)-2*13))
    for i in range(13,len(x)-13):
        for j in range(13,len(x)-13):
            w_f[j-13][i-13] = w[j][i]
    
    o = copy.deepcopy(I)
    for xx in range(26,len(I)-26):
        for yy in range(26,len(I)-26):
            o_w = 0
            for xxx in range(52):
                for yyy in range(52):
                    x = xx + xxx - 26
                    xi = xx - 26
                    y = yy +yyy -26
                    y_xi =yy -26
                    o_w += I[y][x]*w_f[y-y_xi][x-xi]/np.sum(w_f)
                    #print o_w
            o[yy][xx]=o_w
            print ("aaa")
    np.savetxt("w.txt",w_f)
    cv2.imwrite("o.png",o)
    #print Gd1
    plot(x,y,Gd1,Gd2,w)
    np.savetxt("o.txt",o)
    
if __name__ == '__main__':
    main()
