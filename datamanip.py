#/usr/bin/enc python

import numpy as np

#Normalize Data set from 0 to 1
def normalize(z):
    zNormalized = z - z.min()
    zNormalized = zNormalized/zNormalized.max()
    
    return zNormalized

#Remove background noise by removing data below lower limit
def threshBackground(X,z,thresh):
    #X: coordinate
    #z: the weight (mass) corresponding to the coordinates in X
    index = np.where(z > thresh)              
    return [X[index[0],:],z[index[0]]]

