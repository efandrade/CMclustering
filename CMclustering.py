#/usr/bin/env python

import numpy as np
import random


#Initaite the number of centeroids at random
def initialCentroids(X,K):
    #X: coordinate
    #K: the number of centroids to initialize
    
    [m,n] = X.shape
    centroids = np.zeros([K,n])
    
    assign_rand = random.sample(range(0,m),K)
    centroids = X[assign_rand,:]
    
    return centroids
    
#Find the points closes to each centroid
def centroidIdx(X,centroids,z=1):
    #X:         coordinate
    #centroids: coordinates of current centroids
    #z:         the weight (mass) corresponding to the coordinates in X,
    #           if no z is given the weight at every point is the same value: 1
        

    [m,n] = X.shape
    K = centroids.shape[0]
    
    #make matrix with each weight is repeated for each coordinate dimension n
    z = np.tile(z,[n,1]).T    
    
    idx = np.zeros([X.shape[0],1])   
    diff = np.zeros([m,2])
    X_norm2 = np.zeros([m,K])
    
    #calcualte the difference between each point and the centroid weighted by z
    #   for each centroid K
    for i in range(K):
        diff = (X - np.tile(centroids[i,:],[m,1]))/z
        X_norm2[:,i] = np.sum(diff*diff,1)
    
    #Create and index labeling the closes centroid to each coordinate
    idx[:,0] = X_norm2.argmin(1)
    
    return idx
				
#Calculate the new average position for all points assigned to each centroid
def newCentroid(X,centroids,idx,z=1):
    #X:         coordinate
    #centroids: coordinates of current centroids
    #idx:       index labeling the closes centroid to each coordinate
    #z:         the weight (mass) corresponding to the coordinates in X,
    #           if no z is given the weight at every point is the same value: 1

    n = X.shape[1]
    
    #make matrix with each weight is repeated for each coordinate dimension n
    z = np.tile(z,[n,1]).T
				
    K = centroids.shape[0]
    mu = np.zeros(centroids.shape)
    
    #For each point corresponding to a centroid, calculating the center of mass
    #   for those points
    for i in range(K):
        mu[i] = (1/sum(z*(idx==i)))  * np.sum(z * X * (idx == i),0)
        
    return mu
