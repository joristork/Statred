#!/usr/bin/env python
"""
:synopsis:  Analysis of local structure of an image (lab exercise 5.3). Uses
            the incremental method for calculating the covariance derived in
            exercise 5.1
            

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import matplotlib.pyplot as plt
import numpy as np
import os
import sys


def eigsorted(X):
    """ Returns the eigenvectors and eigenvalues sorted in descending order """

    l, V = np.linalg.eig(X)
    si = np.argsort(l)[-1::-1]
    return l[si], V[:,si]


def plotter(nr, data):
    """ Auxiliary function: all required plots, grouped for convenience  """

    if nr is 1:
        x = data
        plt.figure()
        plt.subplot(1,2,1)
        plt.imshow(x, cmap=plt.cm.gray)
        d = x[75:100,170:195]
        plt.subplot(1,2,2)
        plt.imshow(d, cmap=plt.cm.gray)
        plt.savefig('data/image_with_detail.pdf')
    if nr is 2:
        l = data
        plt.figure()
        plt.bar(xrange(len(l)), l)
        plt.savefig('data/5.3_scree.pdf')
    if nr is 3:
        V = data
        plt.figure()
        for j in xrange(6):
            plt.subplot(2,3,j)
            plt.imshow(V[j].reshape(25,25), cmap=plt.cm.gray)
        plt.savefig('data/5.3_eigenvectors.pdf')


def main():
    """
    1. reads image, saves figure: image beside 25x25 detail
    2. finds cov(dataset of all 25x25px details) 
    3. plots scree diagram of eigenvalues of cov. matrix
    4. plots first 6 eigenvectors
    5. saves figure: detail and reconstruction from k eigenvectors

    """

    im = plt.imread('data/image.jpg')[-1::-1,:]          # image (de-flipped)
    h, w = im.shape
    imsize = h*w

    plotter(1, im)
    
    # xi are the details in the image
    xystep = 25                                         # width of one detail
    xisize = xystep * xystep                            # size of one detail
    sxi = np.zeros((xisize,), dtype=float)              # sum of details
    sxixit = np.zeros((xisize,xisize),dtype=float)      # sum(xi * xi.T)
    S = None                                            # covariance matrix
    n = 0.0                                             # nr of details
    X = np.empty((xisize,0))

    S_alt = None

    if os.path.isfile("data/5.3_cov.npy"):              # try to recycle old S
        S = np.load("data/5.3_cov.npy")
    else:                                               # or else calculate S
        for j in xrange(h - xystep+1):
            for k in xrange(w - xystep+1):
                xi = im[j:j+xystep, k:k+xystep].reshape(xisize)
                # X = np.append(X, xi.reshape(xisize,1), axis=1)
                sxi += xi
                sxixit += np.outer(xi, xi)

                if n % 1 == 0:
                    print 'xi: \n', xi
                    print 'n: \n', n
                    print 'sxi: \n', sxi
                if n > 1:
                    sys.exit(0)
                n += 1.0

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
        np.save('data/5.3_cov.npy', S)
    print '\nS: \n', S
    # print '\nnp.cov(X)\n', np.cov(X)
    l, V = eigsorted(S)

    plotter(2, l)
    plotter(3, V)


if __name__ == "__main__":
    main()
