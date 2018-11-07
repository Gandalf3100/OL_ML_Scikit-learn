# To better understand Machine Learning, I am using sklearn and making an
# example with Orange and Apple. So the mathematical problem is how would 
# you create an algorithme that can see/find out what your data belongs to.
# So befor we start the algorithem need some Training data:
#
#   Weight  Texture     Label
#   140g    Smooth = 1  Apple = 0 
#   130g    Smooth = 1  Apple = 0
#   170g    Bumpy = 0  Orange = 1
#   150g    Bumpy =0   Orange = 1
#
# We use a clasifier and we need these data to train our clasifier. 
# The more data the better a clasifier our clasifier will be.
# 
# In the program below the "features" are the input to the clasifier and the
# "labels" are the output we wish to see.
#
# eg. if the data given to the clasifier is " 140g and Smooth " we want the 
# lable to say "0 or Apple".
# 
# So now we are Creating a "Decision Tree". The clasifier can be seen "as a 
# box of rules" . So to start out with our Decision tree, This will be an 
# empty set of rules, so ths is why we need to load our training data, this 
# will create/setup the our decision tree.
#
# The creator of sickit has a training algorithme, wich is include in the 
# clasifier object, and is called "fit" or "Find Data and Patten."
# So now we will give the "Decision Tree" a task what is this "150 and 0" or
# "150g and Bumpy" we are hoping that it will say Orange or write "1"
#
# Try to run this script. hallo-world.py
#
# The clasifier predict gives us the result.
# INFO: Decision Trees (DTs) are a non-parametric supervised learning method used 
# for classification and regression. The goal is to create a model that predicts
# the value of a target variable by learning simple decision rules inferred 
# from the data features.

from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[150, 0]])

# NEXT STEP is to play with IRIS data set

#import graphviz 
#dot_data = tree.export_graphviz(clf, out_file=None) 
#graph = graphviz.Source(dot_data) 
#graph.render("labels") 
