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
    print u'\n Please enter the elements of the mean vector \u03BC'
    m = np.zeros((4), dtype=np.int )
    m[0] = raw_input(u'\n \u03BC[0] >> ')
    m[1] = raw_input(u'\n \u03BC[0] >> ')
    m[2] = raw_input(u'\n \u03BC[0] >> ')
    m[3] = raw_input(u'\n \u03BC[0] >> ')

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
