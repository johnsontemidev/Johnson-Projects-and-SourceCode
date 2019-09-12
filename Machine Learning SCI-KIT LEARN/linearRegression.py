# ============ Data Science, Algorithms and Advanced Software Engineering ===============
# ============ Johnson Temilola - [2019/08/03] ===========

# ============ Program Description ===================
'''
   Using the diabetes dataset to perform linear regression.
   Instead of using linear_model.LinearRegression() from sklearn,
   create your own function to return the gradient and the best-fit line y-intercept.
      . m = (μ(x) (y) μ(m = * μ − x * y))/((μ(x))² − μ(x²))
      . b = μ(y) − m * μ(x)
      . Where μ is a mean function
     
   Reserve the last 20 observations for testing and use the rest for training your model.

   Produce a figure with the following:
   Scatter plot of training data colored red.
   Scatter plot of testing data colored green.
   Line graph for the best-fit line colored blue.
   Legend
 
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

def getLinearRegFit(x, y):
    # to calculate μ (the mean)
    mean_x = np.mean(x)
    mean_x2 = np.mean(x**2)
    mean_y = np.mean(y)
    mean_xy = np.mean(x*y)
    
    # to calculate the slope and intercept of line
    m = (mean_x*mean_y - mean_xy) / (mean_x**2 - mean_x2)
    b = mean_y - m*mean_x
    
    # to return line parameters
    return m, b

def getPred(x, m, b):
    
    # yhat = slope * x + b
    return m*x + b
    
if __name__ == "__main__":
    # to load the data
    dia_data = datasets.load_diabetes()
    
    # getting the features and target
    x, y = dia_data.data[:,2], dia_data.target
    
    # Splitting into train and the test data
    trainX, testX = x[:-20], x[-20:]
    trainY, testY = y[:-20], y[-20:]
    
    # Getting the best Fit line
    m, b = getLinearRegFit(trainX, trainY)
    
    # get predictions for the test set
    predY = getPred(testX, m, b)
    
    # Plot the results
    plt.scatter(trainX, trainY, color = "red")
    plt.scatter(testX, testY, color = "green")
    plt.plot(x, getPred(x, m, b), color = "blue")
    plt.legend(["Best Fit Line", "Training Data", "Test Data"])
    plt.xlabel("Body Mass Index")
    plt.ylabel("Target")
    
    plt.show()
