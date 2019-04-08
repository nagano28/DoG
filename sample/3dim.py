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

I = np.zeros((300,300))
for j in range(150):
   for i in range(150):
      I[j][i] = 230
   for i in range(150,300):
       I[j][i] = 100
for j in range(150,300):
   for i in range(150):
      I[j][i] = 100
   for i in range(150,300):
       I[j][i] = 230

cv2.imwrite("1.png",I)

img2 = np.zeros((248,248))
img = cv2.imread("1.png",0)
for i in range(26,248+26):
    for j in range(26,248+26):
        img2[j-26][i-26]=img[j][i]
        
x = np.arange(0,len(img2))
y = np.arange(0,len(img2))
X,Y = np.meshgrid(x, y)
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('pixel value')
#ax.plot_wireframe(X, Y, Gd1, color="r")
#ax.plot_wireframe(X, Y, Gd2, color="b")
ax.plot_wireframe(X, Y, img2, color="b")
plt.savefig("1_meth.png")
plt.show()

