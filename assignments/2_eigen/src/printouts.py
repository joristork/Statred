#!/usr/bin/env python

"""
:synopsis:  Provides informative printouts.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"


def printout24(Y, S, m, estm, estS, S_M, m_M, Msize):
    print '\nDistribution:'
    print '|\n| Mean:'
    print '| \t',m,'\n|'
    print '| Covariances:\n|'
    print '| \t',S[0]
    print '| \t',S[1]
    print '| \t',S[2]
    print '| \t',S[3]
    print "\nEstimate of (m,S) from one sample of size %s:" % str(Y.shape[1])
    print "|\n| Mean:\n|"
    print '|\t',estm
    print "|\n| Covariances:\n|"
    print '|\t',estS[0]
    print '|\t',estS[1]
    print '|\t',estS[2]
    print '|\t',estS[3]
    print "\nBehaviour across %d samples ~ N(m,S):" % Msize
    print "|\n| Mean of %d means (note: closer to actual mean):\n|" % Msize
    print '|\t',m_M
    print "|\n| Covariances for %d means (note: smaller values):\n|" % Msize
    print '|\t',S_M[0]
    print '|\t',S_M[1]
    print '|\t',S_M[2]
    print '|\t',S_M[3]
    print '\n'
