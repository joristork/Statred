from pylab import *
from svmutil import *

class SVMClassifier:
    def __init__(self, X, c, parameter):
        self.model = svm_train(c.tolist(), X.tolist(), parameter)

    def classify(self, x):
    
        # svm_predict is a function from svmutil, it is intended to classify an
        # entire test set a once. To classify just one sample we need the first
        # element of labels.
        labels, _, _ =  svm_predict([0], [x.tolist()], self.model)
        return labels[0]
        
        
# The colors
colors = ['black', 'blue', 'brown', 'gray', 'green', 'orange', 'pink', 'red',
          'violet', 'white', 'yellow']
        
lines = open("natural400_700_5.asc").readlines()

D = zeros((0, 61))
y = array([])

for i in range(0, len(lines), 2):
   
    ind = None
    
    for j, color in enumerate(colors):
        if lines[i].find(color) >= 0:
            ind = j
     
    if ind is not None:
        d = fromstring(lines[i+1], dtype=int, sep=" ")
        D = append(D, array([d]), axis=0)
        y = append(y, ind)
        
    

# Get random indices of the learn set and the test set. The test set is one 
# third of the complete dataset and the learn set is two third.
N = len(D)
ind = permutation(arange(0, N))

T = ind[:N/3] # Test set
L = ind[N/3:] # Learn set


# Construct the classifier, for more information about these parameters please
# see the output of the easy script in 'easy_results/natural/natural.easy.model'.
param = '-c 32768.0 -g 0.0001220703125'

classifier = SVMClassifier(D[L], y[L], param)


# Create a confusion matrix
CM = zeros((len(colors), len(colors)))

for i in ind:
    c = classifier.classify(D[i])
    CM[int(y[i]), int(c)] += 1


# Print the confusion matrix
print 'Confusion matrix'

for i in range(-1, len(colors)):
    for j in range(-1, len(colors)):
    
        if i == -1 and j == -1:
            print '%10s' % '',
        elif i == -1:
            print '%10s' % colors[j],
        elif j == -1:
            print '%10s' % colors[i],
        else:
            print '%10d' % CM[i, j],

    print
