# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 17:04:42 2018

@author: Nagano Masatoshi
"""
import numpy as np
from math import exp, sqrt, pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
    """
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            ax.scatter(x[i], y[j], Gd1[j][i], color="r")
            ax.scatter(x[i], y[j], Gd2[j][i], color="r")
            ax.scatter(x[i], y[j], w[j][i], color="g")
    """
    #ax.plot(x, y, Gd1, "o", color="r")
    #ax.plot(x, y, Gd2, "o", color="b")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('w')
    """
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            ax.plot_wireframe(x[i], y[j], Gd1[j][i], color="r")
            ax.plot_wireframe(x[i], y[j], Gd2[j][i],  color="b")
            ax.plot_wireframe(x[i], y[j], w[j][i], color="g")
    """
    #ax.plot_wireframe(X, Y, Gd1, color="r") #gauss 1
    #ax.plot_wireframe(X, Y, Gd2, color="b") #gauss 2
    ax.plot_wireframe(X, Y, w, color="g") #gauss 1 & 2
    #ax.plot_wireframe(x[i], y[j], Gd2[j][i],  color="b")
    #ax.plot_wireframe(x[i], y[j], w[j][i], color="g")
    #plt.plot(x,Gd1,"r")
    #plt.plot(x,Gd2,"b")
    #plt.plot(x,w,"g")
    #plt.xlim([-8,8]) # x軸の範囲を指定
    #plt.ylim([-0.5,1]) # y軸の範囲を指定
    plt.savefig("DoG_1&2-3dim.png")
    plt.show()

def main():
    #パラメータ
    sig_ex = 1
    sig_in = 2
    c_ex = 1.5
    c_in = 1
    
    #x,yの範囲
    x = np.arange(-7.5,8.0,0.2)
    y = np.arange(-7.5,8.0,0.2)
    Gd1 = np.zeros((len(y),len(x)))
    Gd2 = np.zeros((len(y),len(x)))
    w = np.zeros((len(y),len(x)))
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            Gd1[j][i],Gd2[j][i],w[j][i] = DoG(sig_ex, sig_in, c_ex, c_in, x[i], y[j])
    #print Gd1
    plot(x,y,Gd1,Gd2,w)
    #np.savetxt("a.txt",w)
if __name__ == '__main__':
    main()
