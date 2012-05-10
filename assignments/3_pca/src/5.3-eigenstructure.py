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


def main():
    a = plt.imread('yard.jpg')[::-1,:] # image flipped ...
    print a.shape
    plt.figure(1)
    plt.subplot(1,2,1)
    plt.imshow(a, cmap=plt.cm.gray)
    d = a[75:100,170:195]
    plt.subplot(1,2,2)
    plt.imshow(d, cmap=plt.cm.gray)
    plt.savefig('yard_with_detail.pdf')
    print d.shape
    
    sstep = 25
    ssize = sstep * sstep
    ssum = np.zeros((ssize,), dtype=float)
    sxxt = np.zeros((ssize,ssize),dtype=float)
    h, w = a.shape
    aflat = a.reshape(h*w,)
    print np.cov(a)
    exit(0)
    for i in xrange(h - sstep):
        for j in xrange(w - sstep):
            xi = a[i:i+sstep, j:j+sstep].reshape(ssize,)
            ssum = ssum + xi
            sxxt = sxxt + np.outer(xi, xi)
    m = ssum / 53824.0 
    S = (sxxt - 5324.0 * np.outer(m,m)) / (53824.0 - 1)
    np.save('5.3_cov.npy', S)
    print S


if __name__ == "__main__":
    main()
