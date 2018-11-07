# This is the next part, here we are going to play with the plant "iris" this is dataset that is includede 
# from sklearn in contains 150 examples devided in theer types. 
# You can see the data here https://en.wikipedia.org/wiki/Iris_flower_data_set click on data, in consist of 
# 150 dataset. sklearn has also the command to call the data is included.

# About Numpy. Adds Python support for large, multi-dimensional arrays and matrices, along with a large library 
# of high-level mathematical functions to operate on these arrays.

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
# About the dataset provided with iris, they are devided into three types of iris 0-50 setosa 50-100 versicolor 
# 100-150 virginic
# So here we are selecting one of each.
test_idx = [0, 50, 100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# NOW WE WILL TEST WITH OUR TEST DATA
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print "TEST_TARGET ",test_target
print "PREDICTION ",clf.predict(test_data)
#Here we try our test data 0 or 1 or 2

print "BASED ON THE TEST DATA, WHAT IT IS PREDICTING 0=setosa 1=versicolor 2=virginica" 
print iris.feature_names, iris.target_names
for i in range(len(test_target)):
	print "WHAT IS THIS: ",test_data[i]," Prediction : ", test_target[i]
	

