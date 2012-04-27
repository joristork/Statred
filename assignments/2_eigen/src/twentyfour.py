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
    data = np.load("data.npy", 'r').T
    print data
    original_cov = np.load("cov.npy", 'r')
    original_mean = np.load("mean.npy", 'r')

    print "The dataset contains " + str(data.shape[0]) + " samples."

    print "\nEstimation of the mean:\n"
    mean = np.mean(data, axis = 0)
    print mean

    print "\nOriginal mean:\n"
    print original_mean    

    print "\nCompare to original mean (estimate - original):\n"
    print (mean - original_mean)
    

    print "\nEstimation of the covariance matrix\n"
    cov = covariance(data)
    print cov

    print "\nOriginal covariance:\n"
    print original_cov


    print "\nCompare to original covariance (estimate - origional):\n"
    print cov.T - original_cov



    print "\nStart estimating mu repeatedly\n"
    means = []
    nmeans= 100
    for i in xrange(nmeans):
        means.append(np.mean(data[i * data.shape[0] / nmeans : (i+1)*nmeans - 1], axis = 0).tolist())
    ms = np.array(means)

    print "\nThe covariance has become smaller, as expected:\n"
    data =  covariance(ms)
    print data

if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 2 | exercise 24 ***\n'
            
    main()
