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
import sys
import os


def mean(data):
    return np.mean(data, axis=0)


def covariance(data):
    m = mean(data)
    d = data - m
    return np.sum(map(lambda x: np.outer(x, x), d), axis = 0) / (len(data) - 1.0)

def main():
    print '\n --- Sample generator --- '
    data_file = 'data.npy' # used to store the generated data for assignment 24'
    m = np.array([[2], [5], [5], [2]])
    print '\n mu:'
    print m
    S = np.array([[1,3,2,4], [3, 3, 1, 2], [2, 1, 2, 1], [4, 2, 1, 3]])
    print '\n Sigma:'
    print S
    d, U = np.linalg.eig(S) 
    L = np.diagflat(d) # Lambda. 4x4 matrix with eigenvalues on diagonal
    X = np.random.randn(4, 1000) # random samples from N(0,1)
    A = np.dot(U, np.sqrt(np.abs(L))) # interim matrix
    Y = np.dot(A,X) + np.tile(m, 1000) # add mu to each sample adjusted by A
    np.save(data_file, Y)
    print '\n Data written to %s\n' % data_file




    # prompt for covariance matrix
    #
    # generate data matrix
    #
    # draw 12 scatter plots 
    #for i in xrange(4):
    #    for j in xrange(4):
    #        if i is not j:
    #            """ draw samples  """
    #            plt.subplot(4,4,(1 + j+(i*4)) )
    #            plt.plot(,,'ro', ms=3.0)

    #            """ draw means """
    #            plt.plot(, , marker='+',c='black', ms=15.0)


    #plt.show()

    #np.save('data.npy', data)


if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 2 ***\n'
            
    main()
