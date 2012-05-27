#!/usr/bin/env python
"""
:synopsis:  calculates cov. iteratively using uses formula from '5.1-proof.pdf'
            
.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import numpy as np


def iter_cov(m, X):
    """ calculates covariance iteratively """

    sxxt = np.zeros((m.size,m.size), dtype=float)
    for xi in X.T:
        sxxt += np.outer(xi, xi)
    return (sxxt - X.shape[1] * np.outer(m, m)) / (X.shape[1] - 1)
