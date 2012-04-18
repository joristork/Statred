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
    m = mean(data)
    d = data - m
    return np.sum(map(lambda x: np.outer(x, x), d), axis = 0) / (len(data) - 1.0)

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
