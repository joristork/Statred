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

    return np.mean(data, axis=1).reshape(np.shape(data)[0], 1)


def covariance(data):
    m = mean(data)
    d = data - m
    temp = np.zeros((np.shape(data)[0],np.shape(data)[1],np.shape(data)[0]),dtype=float)
    for i in xrange(np.shape(data)[1]):
        temp[:,i] = np.outer(data[:,i], data[:,i])
    return np.sum(temp, axis = 1) / (np.shape(data)[1] - 1.0)


def main():
    data = np.load("data.npy", 'r')
    S = np.load("cov.npy", 'r')
    m = np.load("mean.npy", 'r')

    print '\nOur generated sample:\n'
    print data
    print "\nThe sample contains " + str(data.shape[1]) + " data points."

    estm = mean(data)
    print "\nDifference between means: estimate from sample minus original:\n"
    print (estm - m)

    estS = covariance(data)
    print "\n Difference between covariance matrices: estimate from sample minus original:\n"
    print (estS - S)

    print "\n\nEstimating mu repeatedly...\n"
    means = []
    nmeans= 100
    for i in xrange(nmeans):
        means.append(np.mean(data[i * data.shape[0] / nmeans : (i+1)*nmeans - 1], axis = 0).tolist())
    ms = np.array(means)

    print "The covariance has become smaller, as expected:\n"
    data =  covariance(ms)
    print '%s\n' % str(data)

if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 2 | exercise 24 ***\n'
            
    main()
