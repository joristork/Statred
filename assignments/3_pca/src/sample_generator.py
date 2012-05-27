#!/usr/bin/env python

"""
:synopsis:  lab exercise 23, statistical reasoning class (2012/UvA/Netherlands)

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import matplotlib.pyplot as plt
import numpy as np
import sys
import os


def generate():
    """ generates data from a normal distribution """

    m = np.array([2., 5., 5., 2.])
    temp = 2.0 * (np.random.rand(4, 4)) # to random-generate S
    S = np.dot(temp, temp.T) # make sure S is positive semidefinite, symmetric
    d, U = np.linalg.eig(S)
    L = np.diagflat(d)
    A = np.dot(U, np.sqrt(L))
    X = np.random.randn(4, 1000)
    Y = np.dot(A,X) + np.tile(m.reshape(4,1), 1000) 
    return S, m, Y


def main():
    S, m, Y = generate()

    #draw 12 scatter plots 
    for i in xrange(4):
        for j in xrange(4):
            if i is not j:
                """ draw samples  """
                plt.subplot(4,4, 1 + j + i * 4)
                plt.plot(Y[i], Y[j], 'ro', ms=2.0)
    plt.show()


if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 2 ***\n'
    print '\nDone generating samples!\n'
    main()
