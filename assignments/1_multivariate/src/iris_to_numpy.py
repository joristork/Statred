#!/usr/bin/env python

"""
:synopsis:  Converts the iris dataset text file to a numpy array.

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import sys
import os
from numpy import loadtxt

def convt(s):
    tab = {'Iris-setosa':1.0, 'Iris-versicolor':2.0, 'Iris-virginica':3.0}
    if tab.has_key(s):
        return tab[s]
    else:
        return -1.0

def load_iris():
    return loadtxt('iris.data', delimiter = ',', dtype = float, converters = {4:convt})

