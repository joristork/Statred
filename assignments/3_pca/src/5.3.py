#!/usr/bin/env python
"""
:synopsis:  PCA of local structures of an image (lab exercise 5.3). 

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import matplotlib.pyplot as plt
import numpy as np
from print_plot import plot53
from iter_cov import iter_cov


def eigsorted(X):
    """ Returns the eigenvectors and eigenvalues sorted in descending order """

    l, V = np.linalg.eig(X)
    si = np.argsort(l)[-1::-1]
    return l[si], V[:,si]


def optimal_k(l):
    """ estimates an optimal number of eigenvectors for reconstruction """

    ltotal = np.sum(l)
    klsum = 0.0
    k = 0.0
    while (klsum / ltotal) < 0.99:
        klsum += l[k]
        k += 1.0
    return k


def eigen_reconstruct(detail, m, k, V):
    """ returns the detail reconstructed from first k eigenvectors """
    
    X = detail.reshape(detail.size,)
    Y = np.dot(V.T, X - m)
    kX = np.dot(V[:,:k], Y[:k]) + m
    return kX.reshape(detail.shape)
    

def main():
    """
    1. reads image, saves figure of image + detail
    2. finds covariance matrix for details
    3. plots scree diagram
    4. plots first 6 eigenvectors
    5. saves figure of detail and its eigenreconstruction 

    """

    im = plt.imread('data/image.jpg')[-1::-1,:]
    h, w = im.shape
    
    xiw = 25
    xih = 25
    xisize = xiw * xih                        
    X = np.empty((xisize, (h-xih+1)*(w-xiw+1)))  # holds all details

    for j in xrange(h - xih + 1):
        for k in xrange(w - xiw + 1):
            xi = im[j:j+xih, k:k+xih].reshape(xisize)
            X[:,j*xiw+k-1] = xi

    m = np.mean(X, axis=1)
    S = iter_cov(m,X)
    l, V = eigsorted(S)

    k = optimal_k(l)
    detail = im[75:100, 170:195]
    kdetail = eigen_reconstruct(detail, m, k, V)

    plot53(im, l, V, detail, kdetail)


if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 3 | 5.3 ***\n'
    print '--> Performing all calculations. This may take a minute...\n'
    main()
