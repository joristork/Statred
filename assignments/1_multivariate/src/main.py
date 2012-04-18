#!/usr/bin/env python

"""
:synopsis:  

.. moduleauthor:: Joris Stork <joris@wintermute.eu>, Lucas Swartsenburg
<luuk@noregular.com>

"""

__author__ = "Joris Stork, Lucas Swartsenburg"

import sys
import os
import dbl # debugging


def menu():
    os.system(['clear','cls'][os.name == 'nt'])
    """ The main menu. ``fails''= number of invalid choices """
 
    print '\n --- MAIN MENU ---'
    print '\n [1] '
    print '\n [2] '
    print '\n [3] Exit'
    fails = 0

    def prompt(fails):
        """Note that we ensure ``choice'' is not interpreted as a string"""
        choice = raw_input('\nChoose activity:\n>> ')
        router(choice, fails)

    def router(choice, fails):
        """ Executes the desired choice, if it is valid """
        if choice == '1':
            run_forest_fire()
        elif choice == '2':
            if len(sys.argv) != 3:
                print >> sys.stderr, "usage: %s <No. Predators> <No. Preys> <Initial energy predator> <Initial energy prey> <Energy decrease predator> <Energy increase prey> <treshold predator> <treshold prey> (<grid widht> <grid height> <maxgen>)) " % sys.argv[0]    
            predator_prey(sys.argv)
        elif choice == '3':
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


if __name__ == "__main__":
    print '\n*** Statistisch redeneren: assignment 1 ***\n'

            
    menu()
