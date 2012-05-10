#!/usr/bin/env python
"""
:synopsis:  Uses the incremental method for calculating the covariance derived
            in exercise 5.1, to obtain the covariance matrix for the set of
            25x25 details in a 256x256 image. Then plots the scree diagram of
            eigenvalues of the covariance matrix, and plots the eigenvectors
            as images. Finally, reduces the dimensionality of a detail with
            respect to the principal component basis, and uses the result to
            reconstruct a similar detail in the original coordinate system.
            

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import matplotlib.pyplot as plt
import numpy as np
import os


def main():
    """
    1. reads image
    2. takes detail
    3. saves figure with image beside detail
    4. finds covariance of elements of the sample that consists of all 25x25px
        details of the image.
    5. saves scree diagram of eigenvalues of covariance matrix from (4)
    6. saves plots of first 6 eigenvectors
    7. displays detail and its reconstruction from k eigenvectors

    """

    x = plt.imread('yard.jpg')[::-1,:] # image flipped ...
    h, w = x.shape
    xsize = h*w

    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(x, cmap=plt.cm.gray)
    d = x[75:100,170:195]
    plt.subplot(1,2,2)
    plt.imshow(d, cmap=plt.cm.gray)
    plt.savefig('yard_with_detail.pdf')
    
    xystep = 25
    xisize = xystep * xystep # 
    sxi = np.zeros((xisize,), dtype=float) # sum of measurements
    sxixit = np.zeros((xisize,xisize),dtype=float) # holds sum(xi * xi.T)
    S = None
    n = 0.0
    if os.path.isfile("5.3_cov.npy"):
        S = np.load("5.3_cov.npy")
    else:
        for j in xrange(h - xystep+1):
            for k in xrange(w - xystep+1):
                n += 1
                xi = x[j:j+xystep, k:k+xystep]
                if j == 75 and k == 170:
                    plt.figure()
                    plt.subplot(1,1,1)
                    plt.imshow(xi, cmap=plt.cm.gray)
                    plt.savefig('samedetail.pdf')
                if j*k == 10000:
                    plt.figure()
                    plt.subplot(1,1,1)
                    plt.imshow(xi, cmap=plt.cm.gray)
                    plt.savefig('randetail.pdf')
                if j*k == 20000:
                    plt.figure()
                    plt.subplot(1,1,1)
                    plt.imshow(xi, cmap=plt.cm.gray)
                    plt.savefig('randetail2.pdf')
                if j*k == 30000:
                    plt.figure()
                    plt.subplot(1,1,1)
                    plt.imshow(xi, cmap=plt.cm.gray)
                    plt.savefig('randetail3.pdf')
                xi = xi.reshape(xisize)
                sxi += xi
                sxixit += np.outer(xi, xi)

        m = sxi / n
                
        print '\nn: ', n
        print '\nsxi.shape: ', sxi.shape
        print '\nsxixit.shape: ', sxixit.shape
        print '\nsxi: \n', sxi
        print '\nsxixit: \n', sxixit
        print '\nnp.outer(m,m): \n', np.outer(m,m)
        print '\nn * np.outer(m,m): \n', n * np.outer(m,m)
        print '\nm: \n', m

        S = (sxixit - (n * np.outer(m,m))) / (n - 1.0)
        np.save('5.3_cov.npy', S)
    print '\nS: \n', S
    l, V = np.linalg.eig(S)
    si = np.argsort(l)[::-1]
    l = l[si]
    V = V[:,si]
    plt.figure()
    plt.bar(xrange(len(l)), l)
    plt.savefig('5.3_scree.pdf')
    plt.figure()
    for j in xrange(6):
        plt.subplot(2,3,j)
        plt.imshow(V[j].reshape(25,25), cmap=plt.cm.gray)
    plt.savefig('5.3_eigenvectors.pdf')


if __name__ == "__main__":
    main()
