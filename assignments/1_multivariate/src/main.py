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


def print_mean_covariance():
    data = load_iris()
    print '\nMean (overall):\n%s' % str(mean(data))
    print '\nCovariance (overall):\n%s' % str(covariance(data))

    print '\nMean (setosa):\n%s' % str(mean(data[:50]))
    print '\nCovariance (setosa):\n%s' % str(covariance(data[:50]))

    print '\nMean (versicolor):\n%s' % str(mean(data[50:100]))
    print '\nCovariance (versicolor):\n%s' % str(covariance(data[50:100]))

    print '\nMean (virginica):\n%s' % str(mean(data[101:150]))
    print '\nCovariance (virginica):\n%s' % str(covariance(data[101:150]))

    raw_input('\nPress Enter')
    menu.run()


def plot_iris_means_covariance():
    """ iris samples, means  """
    data = load_iris()
    data_m = mean(data)
    setosa = data[:50]
    setosa_m = mean(setosa)
    versicolor = data[50:100]
    versicolor_m = mean(versicolor)
    virginica = data[100:150]
    virginica_m = mean(virginica)

    """ covariance ellipse (unfinished) """
    phi = np.arange(0, 2 * np.pi, 0.01)
    r_1 = np.outer(np.array([1,0,0,0]), np.cos(phi))
    r_2 = np.outer(np.array([0,1,0,0]), np.sin(phi))
    r = np.transpose(r_1 + r_2)
    ones = np.ones((len(phi),), dtype=float)
    C = covariance(data[:,:4])
    print '\ntest: \n', np.cov(data[:,:4]) == covariance(data[:,:4])
    temp1 = map(lambda x : C * x, r)
    for i in xrange(len(temp1)):
        ellipse = np.inner(r[i], temp1[i])
    x = mean(data[:,:4])
    ellipse = x + np.sqrt(ellipse)

    for i in xrange(4):
        for j in xrange(4):
            if i is not j:
                """ draw samples  """
                plt.subplot(4,4,(1 + j+(i*4)) )
                plt.plot(setosa[:,i],setosa[:,j],'ro', ms=3.0)
                plt.plot(versicolor[:,i],versicolor[:,j],'go', ms=3.0)
                plt.plot(virginica[:,i],virginica[:,j],'bo', ms=3.0)

                """ draw means """
                plt.plot(data_m[i], data_m[j],marker='+',c='black', ms=15.0)
                plt.plot(setosa_m[i], setosa_m[j],marker='+',c='r', ms=15.0)
                plt.plot(versicolor_m[i], versicolor_m[j],marker='+',c='g',ms=15.0)
                plt.plot(virginica_m[i], virginica_m[j],marker='+',c='b',ms=15.0)

                """ draw ellipse  """
                #plt.plot(ellipse)

    plt.show()
    menu.run()


def visualise_covariance():
    

    menu.run()


if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 1 ***\n'
            
    menu.run()
