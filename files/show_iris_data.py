# Here we are going to display all the data in the load_iris that sklearn has 
# included. We are going to play with the plant "iris" there are three types.
# You can see the data here https://en.wikipedia.org/wiki/Iris_flower_data_set 
# click on data, in consist of 150 dataset.
# sklearn has also the command to call the data is included.
#
# Here we are loading the data set.
from sklearn.datasets import load_iris
iris = load_iris()

# Here we are going to displaying the data
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]

# Here we running through the 150 records, and displaying them
for i in range(len(iris.target)):
        print "Example %d: lable %s, features %s" % (i, iris.target[i], iris.data[i])

