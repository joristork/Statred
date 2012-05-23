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
import twentythree
import printouts


def covariance(Y):
    m = np.mean(Y, axis=1)
    Yzm = Y - np.tile(m.reshape(Y.shape[0], 1), Y.shape[1])
    return np.dot(Yzm, Yzm.T) / (Yzm.shape[1] - 1.0)


def main():
    S, m, Y = twentythree.generate()

    estm = np.mean(Y, axis=1)
    estS = covariance(Y)

    # we repeat the estimates for multiple Y ~ N(m,S)
    M = np.empty((m.shape[0],0)) 
    for i in xrange(500):
        mi = np.mean(twentythree.generate()[2], axis=1)
        M = np.append(M, mi.reshape(m.shape[0],1), axis=1)
    S_M = covariance(M)
    m_M = np.mean(M, axis=1)

    printouts.printout24(Y, S, m, estm, estS, S_M, m_M, M.shape[1])


if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 2 | exercise 24 ***'
    main()
