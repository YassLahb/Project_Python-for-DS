# Project_Python-for-DS
Project of Python for Data Science and Analysis. Online shoppers Intention.

# Main goal of the project : 
The main goal of this project is to analyze the dataset and visualize it so that we are able to see the main features that we need through using multiple libraries(matplotlib, seaborn, bokeh...) and do some modelling to design a machine learning classification system, that is able to predict an online shopper's intention(buy or no buy), based on the values of the given features and using libraries like scikit-learn through using multiple algorithms and comparing between them. Finally, we will transform the model into a Django API so that it can be displayed properly through it.

# Data Source : 
https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset

# Conclusion : 
In this project, we used Online Shoppers Intention dataset to build models that can classify website visitor, and predict which of them is likely going to make a purchase on the website. 5 different learning classifiers (Logistic Regression, Random Forest, Gradiant Boosting, and Adaboosting) were tested and optimized, and we have achieved the best classification performance using Gradient Boost classifier, followed by random Forest, and then Adaboost.

The best classification performance:

Accuracy: 91%

F1 Score: 0.66

Note: There is a clear difference of classification performance between the 2 classes, that is meanly due to the unbalanced nature of our dataset, where around 85% of our data points belong to 1 class, and less than 15% belong to the other.
