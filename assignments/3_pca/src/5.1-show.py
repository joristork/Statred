#!/usr/bin/env python
"""
:synopsis:  shows that the formula derived in '5.1-proof.pdf' can be used to
            calculate S without storing all x_i in memory.
            
            The advantage of the derived formula is that m does not need to be
            subtracted from each sample before the outer product is
            calculated, reducing the complexity by two subtractions times the
            sample size. Furthermore, the mean can be calculated and used
            after the running sum of sample vectors is complete.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import matplotlib.pyplot as plt
import numpy as np


def main():
    samples = 10000
    dim = 4
    m = np.array([2.0, 5.0, 5.0, 2.0])
    randmat = 1.0 + (np.random.rand(dim,dim))
    S = np.dot(randmat, randmat.T) # make sure S is positive semidefinite, symmetric
    x = np.random.multivariate_normal(m, S, samples).T

    print '\n We will derive the covariance matrix of the following %s dataset...\n' % str(np.shape(x))
    print x
    print '\n... generated from the covariance matrix:\n'
    print S
    print '\nThe calculation will not store all x_i in memory...\n'
    print 'Result:\n'

    sxxt = np.zeros((dim,dim), dtype=float)
    for xi in x.T:
        sxxt += np.outer(xi, xi)
    S_derived = (sxxt - (samples * np.outer(m,m))) / (samples - 1.0)
    
    print S_derived
    print '\nnp.cov(x):\n\n',np.cov(x)


if __name__ == "__main__":
    main()
