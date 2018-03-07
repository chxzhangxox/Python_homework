# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:16:41 2018

@author: chxzh
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img_a = mpimg.imread('a.jpg')
img_b = mpimg.imread('b.jpg')

img_c = img_a.copy()
img_c[250:650, 100:500] = img_b

imgplot_c = plt.imshow(img_c)
plt.axis('off')
plt.savefig('c.jpg')

#============================================================================
img_g = mpimg.imread('g.jpg')
img_h = mpimg.imread('h.jpg')

img_g.astype(np.float)
img_h.astype(np.float)
img_i = np.zeros((img_g.shape[0], img_g.shape[1], img_g.shape[2]), dtype = np.float)

for i in range(img_g.shape[0]):
    for j in range(img_g.shape[1]):
        max_rgb = [np.maximum(img_g[i,j][0],img_h[i,j][0]), np.maximum(img_g[i,j][1],img_h[i,j][1]),np.maximum(img_g[i,j][2],img_h[i,j][2])]
        min_rgb = [np.minimum(img_g[i,j][0],img_h[i,j][0]), np.minimum(img_g[i,j][1],img_h[i,j][1]),np.minimum(img_g[i,j][2],img_h[i,j][2])]
        diff = np.subtract(max_rgb, min_rgb)
        if np.linalg.norm(diff) > 30:
            img_i[i,j] = [diff[2],diff[1],diff[0]]
   
imgplot_i = plt.imshow(img_i, interpolation = 'nearest')
plt.axis('off')
plt.savefig('i.jpg')

#============================================================================

img_d = mpimg.imread('d.jpg')
img_e = mpimg.imread('e.jpg')
imgcopy_d = img_d.copy()
imgcopy_e = img_e.copy()

imgcopy_e[np.logical_and(imgcopy_e[:,:,0] < 50, imgcopy_e[:,:,1] >220, imgcopy_e[:,:,2] < 50)] = 0


for i in range(img_e.shape[0]):
    for j in range(img_e.shape[1]):
        if np.linalg.norm(np.subtract(imgcopy_e[i,j] , [0,0,0])) != 0:
            imgcopy_d[589 + i, 250 + j] = imgcopy_e[i,j]

plt.imshow(imgcopy_d)
plt.axis('off')
plt.savefig('f.jpg')