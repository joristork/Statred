#!/usr/bin/env python
from pylab import *
import sys
import os
from subprocess import *
from svmutil import *

if len(sys.argv) <= 1:
	print('Usage: {0} create_sets [testing_file]'.format(sys.argv[0]))
	raise SystemExit

colors = ['black', 'blue', 'brown', 'gray', 'green', 'orange', 'pink', 'red',
          'violet', 'white', 'yellow']  
                
def containsColor( line ):
    for c in colors:
        if line.find(c)>=0:
            return colors.index(c), c
    return None, None
        
        
#Start source from reader

lines = open(sys.argv[1]).readlines()

traindata_filename = 'trainset'
testdata_filename = 'testset'

trainset = open(traindata_filename, 'w')
testset = open(testdata_filename, 'w')


D = zeros((0, 61))
y = array([])
for i in range(0,len(lines),2):
    ind, c = containsColor(lines[i])
    if ind is not None:
        d = fromstring(lines[i+1],dtype=int,sep=" ")
        D = append(D,array([d]),axis=0)
        y= append(y,ind) 
        
#Calculate how large our dataset is
count_data = len(D)
#Create a random list of indices in the range of our data set
random_i = permutation(arange(0, count_data))
testindices = random_i[:count_data/3] # Test set
trainindices = random_i[count_data/3:] # Learn set

#Write the testdata to a libsvm readable file
for i in testindices:
    t = int(y[i])
    line = "{}: ".format(t)
    for j,val in enumerate(D[i]):
        val_int = int(val)
        line += "{}:{} ".format(j,val_int)
    line += "\n"
    testset.write(line)
testset.close()

#Write the traindata to a libsvm readable file    
for i in trainindices:
    t = int(y[i])
    line = "{}: ".format(t)
    for j,val in enumerate(D[i]):
        val_int = int(val)
        line += "{}:{} ".format(j,val_int)
    line += "\n"
    trainset.write(line)    
trainset.close()

#Easy svm calculates the best kernel and kernelvalues to use on this trainingset. Easy then generates a svm model file which can be loaded to
#make predictions later on. 
cmd = '{0} {1} {2}'.format("python easy.py", traindata_filename, testdata_filename)
print('Using easy.py to train the svm and scale both the train and the test set.')	
f = Popen(cmd, shell = True, stdout = PIPE, stderr = STDOUT).stdout

print "\n\n********** easy.py output **********"
print f.read()
print "\n"

print "Loading " + traindata_filename + ".model " + "to start predicting values."
svm = svm_load_model(traindata_filename + ".model")
print "Loading the scaled testvalues from " + testdata_filename + ".scale."
loaded_labels, scaled_testdata = svm_read_problem(testdata_filename + ".scale")


confusionmatrix = zeros((len(colors), len(colors)))

#Calculate the confusion matrix
percentage = zeros((2, len(colors)))

print "\n\n********** svm_predict function output **********"
for i, data in enumerate(scaled_testdata):   
    labels, _, _ =  svm_predict([0], [data.values()], svm)
    c = labels[0]
    confusionmatrix[int(loaded_labels[i]), int(c)] += 1
    if int(loaded_labels[i]) == int(c):
        percentage[0,loaded_labels[i]] += 1
    else:
        percentage[1, loaded_labels[i]] += 1
print "\n\n"


# Print the confusion matrix
print '********** Confusion matrix ********** '
for i in xrange(-1, len(colors)):
    for j in xrange(-1, len(colors)):
    
        if i == -1 and j == -1:
            print '%10s' % '',
        elif i == -1:
            print '%10s' % colors[j],
        elif j == -1:
            print '%10s' % colors[i],
        else:
            print '%10d' % confusionmatrix[i, j],

    print
    


#Calculate percentages
print"\n\n********** Percentages ********** "
count = 0
good = 0;
for i in xrange(len(colors)):
    total = percentage[0,i] + percentage[1,i]
    count += total
    if total != 0:
        fraction = percentage[0,i] / float(total)
        percent = fraction * 100.0
        print colors[i] + "\t: " + str(percent) + "% correctly predicted"        
    else:
        print colors[i] + "\t: zero occurances, so technically: 100%"
    good += percentage[0,i]


print "Total\t: " + str(((good/count) * 100.0)) + "% correctly predicted"
    
    





