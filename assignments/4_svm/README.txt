For everything to work you need Linux and a couple of packages. In Debian/Ubuntu:
$ sudo apt-get install libsvm-dev libsvm-tools python-libsvm

The main file to execute is fourtyseven.py.

There are a couple of helper files:
easy.py     : A slightly adjusted easy.py file that is provided by Libsvm. This 
              file optimizes the training and test data and creates a model file.
grid.py     : A slightly adjusted grid.py file that is provided by Libsvm. This
              file is used by easy.py.
clean.sh    : A bash script that removes all files created for the svm.
