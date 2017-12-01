import numpy as np
from scipy.misc import imread, imsave
from math import *
import sys



if len(sys.argv) != 9:
     exit(0)

image = imread(sys.argv[1]).astype(np.float32)

#ftiaxnw ton metashmatismo
metasximatismos = [[0,0,0],[0,0,0] ,[0,0,0]]
k = 3
for i in range(2):
    for j in range(3):
        metasximatismos[i][j] = float(sys.argv[k])
        k = k+1

metasximatismos[2][0] = 0
metasximatismos[2][1] = 0
metasximatismos[2][2] = 1
metasximatismos = [[1/2.0,-2.0/3,0],
     [2.0/3,1/2.0,0],
     [0,0,1]]



transformedImage = np.zeros(image.shape)
interpolation = np.zeros(image.shape)
M = image.shape[0]
N = image.shape[1]
m = int(N/2)
n = int(M/2)
theseis = np.zeros((3,M*N))
k=0
for i in range(-m,m+1,1):
    for j in range(-n,n+1,1):

        theseis[0][k]=i
        theseis[1][k]=j
        theseis[2][k]=1
        k=k+1

neesTheseis = np.dot(metasximatismos, theseis)


for i in range(len(neesTheseis[0])):
    neox = neesTheseis[0][i]
    neoy = neesTheseis[1][i]
    if neox.is_integer() and neoy.is_integer():
        if int(neox)+m>=0 and int(neox)+m<M and int(neoy)>=0 and int(neoy)+n<N:
            transformedImage[int(neox)+m][int(neoy)+m] =  image[int(theseis[0][i])+n][int(theseis[1][i])+n]
            interpolation[int(neox)+m][int(neoy)+m] = 1


for i in range(-m,m+1,1):
    for j in range(-n,m+1,1):
        if interpolation[i+m][j+m] == 0:

            nearestD= sqrt(pow(i-neesTheseis[0][0],2)+pow(j-neesTheseis[1][0],2));
            nearest = 0

            for k in range(1,len(neesTheseis[0])):
                if nearestD > sqrt(pow(i-neesTheseis[0][k],2)+pow(j-neesTheseis[1][k],2)):
                    nearest = k
                    nearestD = sqrt(pow(i-neesTheseis[0][k],2)+pow(j-neesTheseis[1][k],2))

            transformedImage[i+m][j+m] =  image[int(theseis[0][nearest])+m][int(theseis[1][nearest])+m]

imsave(sys.argv[2], transformedImage)
