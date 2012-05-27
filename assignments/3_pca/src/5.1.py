#!/usr/bin/env python
"""
:synopsis:  shows that the formula derived in '5.1-proof.pdf' can be used to
            calculate S without storing all x_i in memory.
            
.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import matplotlib.pyplot as plt
import numpy as np
import print_plot
import sample_generator
from iter_cov import iter_cov


def main():
    S, m, X = sample_generator.generate()
    estS = iter_cov(m, X)
    
    print_plot.printout51(X, S, estS)


if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 3 | 5.1 ***\n'
    main()
