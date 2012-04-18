#!/usr/bin/env python

"""
:synopsis:  Functions responding to the descriptions in lab exercise 12 of the
            multivariate random variables chapter (statistisch redeneren, UvA,
            2012).

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import menu
from iris_to_numpy import load_iris
import numpy as np
import sys
import os


def mean(data):
    return np.mean(data, axis=0)

def covariance(data):
    print 'data[0]: '
    print data[0]
    m = mean(data[:,:4])
    print 'm: '
    print m
    d = data[:,:4] - m
    print 'd[0]: '
    print d[0]
    s = np.sum(np.dot(d, np.transpose(d)), axis = 0)
    print s[0]
    return s / (len(data) - 1)

def print_mean_covariance():
    data = load_iris()
    print '\nMean:\n%s' % str(mean(data))
    print '\nCovariance:\n%s' % str(covariance(data))

    raw_input('\nPress Enter')
    menu.run()

def plot_with_means():
    pass

    menu.run()

def visualise_covariance():
    pass

    menu.run()


if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 1 ***\n'
            
    menu.run()
