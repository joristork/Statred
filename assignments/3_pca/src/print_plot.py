#!/usr/bin/env python
"""
:synopsis:  printouts, plots for exercise scripts
            
.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

import numpy as np
import matplotlib.pyplot as plt

__author__ = "Joris Stork, Lucas Swartsenburg"


def printout51(X, S, S_derived):

    print '\nUsing the iterative method, the following covariance matrix:\n'
    print S_derived,','
    print '\nwas estimated from the following %s dataset:\n' % str(np.shape(X))
    print X,','
    print '\ngenerated from the covariance matrix:\n'
    print S,'.'
    print """
The advantage of this iterative method is: 
1.  that m does not need to be subtracted from each sample before the
    outer product is calculated, reducing the complexity by two
    subtractions times the sample size.  
2.  the mean can be calculated and used after the running sum of
    sample vectors is complete, and
3.  the outer products of the samples never need to be stored concurrently 
    in memory 
"""


def plot53(im = None, l = None, V = None, detail = None, kdetail = None):

    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(im, cmap=plt.cm.gray)
    plt.subplot(1,2,2)
    plt.imshow(detail, cmap=plt.cm.gray)
    filename = 'data/image_with_detail.pdf'
    plt.savefig(filename)
    print '\n--> Image and detail saved to %s.\n' % filename

    plt.figure()
    plt.bar(xrange(len(l)), l)
    filename = 'data/5.3_scree.pdf'
    plt.savefig(filename)
    print '--> Scree diagram of eigenvalues saved to %s.\n' % filename

    plt.figure()
    for j in xrange(6):
        plt.subplot(2,3,j)
        plt.imshow(V[j].reshape(25,25), cmap=plt.cm.gray)
    filename = 'data/5.3_eigenvectors.pdf'
    plt.savefig(filename)
    print '--> Eigenvector images saved to %s.\n' % filename

    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(detail, cmap=plt.cm.gray)
    plt.subplot(1,2,2)
    plt.imshow(kdetail, cmap=plt.cm.gray)
    filename = 'data/detail_with_k_reconstruction.pdf'
    plt.savefig(filename)
    print '--> Image and detail saved to %s.\n' % filename
