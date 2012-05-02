#!/usr/bin/env python

"""
:synopsis:  Functions responding to the descriptions in lab exercise 23 and 24
            of the multivariate random variables chapter (statistisch
            redeneren, UvA, 2012).

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys
import os


def main():
    print '\n --- Sample generator --- '
    sample_size = 1000
    dimensions = 4
    data_file = 'data.npy' # used to store the generated data for assignment 24'
    m = np.array([[2], [5], [5], [2]])
    np.save("mean.npy", m)
    print '\n mu:'
    print m
    temp = 1.0 + (np.random.rand(dimensions,dimensions))
    S = np.dot(temp, temp.T) # make sure S is positive semidefinite, symmetric
    np.save("cov.npy", S)
    print '\n Sigma:'
    print S
    d, U = np.linalg.eigh(S) 
    ind = np.argsort(d)
    d, U  = d[ind], U[:,ind]
    L = np.diagflat(d) # Lambda. 4x4 matrix with eigenvalues on diagonal
    A = np.dot(U, pylab.sqrt(np.abs(L))) # interim matrix
    X = np.random.randn(4, sample_size) # random samples from N(0,1)
    Y = np.dot(A,X) + np.tile(m, sample_size) # add mu to each (product of A, sample)
    #Y = np.random.multivariate_normal(m.reshape(4,), S, 1000).T # useful as control
    print Y
    np.save(data_file, Y)
    print '\n Data written to %s\n' % data_file

    #exit(0)

    #draw 12 scatter plots 
    for i in xrange(4):
        for j in xrange(4):
            if i is not j:
                """ draw samples  """
                plt.subplot(4,4,(1 + j+(i*4)) )
                plt.plot(Y[i], Y[j],'ro', ms=3.0)

    plt.show()


if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 2 ***\n'
            
    main()
