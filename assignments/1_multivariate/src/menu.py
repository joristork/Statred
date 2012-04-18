#!/usr/bin/env python

"""
:synopsis:  provides a menu interface

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

from main import print_mean_covariance, plot_with_means, visualise_covariance
import sys
import os


def run():
    os.system(['clear','cls'][os.name == 'nt'])
    """ The main menu. ``fails''= number of invalid choices """
 
    print '\n --- MAIN MENU ---'
    print '\n [1] Show mean and covariance of Iris dataset'
    print '\n [2] Plot Iris dataset with means of set and classes'
    print '\n [3] Visualise covariance matrix'
    print '\n [4] Exit'
    fails = 0

    def prompt(fails):
        """Note that we ensure ``choice'' is not interpreted as a string"""
        choice = raw_input('\nChoose activity:\n>> ')
        router(choice, fails)

    def router(choice, fails):
        """ Executes the desired choice, if it is valid """
        if choice == '1':
            print_mean_covariance()
        elif choice == '2':
            plot_with_means()
        elif choice == '3':
            visualise_covariance()
        elif choice == '4':
            print '\nGoodbye!\n'
            sys.exit(0)
        else:
            tryagain(fails, choice)
        prompt(fails)

    def tryagain(fails, choice):
        """ Gives the user three chances to enter a valid choice """ 
        fails += 1
        if (fails > 2):
            print '\nToo many wrong choices. Exiting...\n'
            sys.exit(0)
        print '\nSorry, ``'+choice+'\'\' is not a valid choice. Try again.'
        prompt(fails)

    prompt(fails)
