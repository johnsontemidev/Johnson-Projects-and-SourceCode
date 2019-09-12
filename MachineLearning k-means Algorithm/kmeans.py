# ========= Data Science, Algorithm and Advanced Software Engineering ======
# ========= Johnson Temilola - [2019/08/06] ==================

# ============ PROGRAM DESCRIPTION ==================
'''
   implement the k-means algorithm and run it on the provided data

   compute the mean (or average) of a number of observations, you simply add all the
observations together and then divide by the number of observations you added
together. The two-dimensional mean is no different. You have a number of x and y
values, so to compute the mean

   ● (x, y) point of a number of points, you simply compute the mean of all the x v alues,
and the mean of all the y values.

   ● the user should decide how many clusters there should be (although, if you are
unsure, it might make sense to begin with just two clusters, and generalize later). The
algorithm will need to run for a user-specified number of iterations, and output:
1.) The number of countries belonging to each cluster
2.) The list of countries belonging to each cluster
3.) The mean Life Expectancy and Birth Rate for each cluster

   In the main iteration loop, for each data point, calculate the squared distance between
each point and the cluster mean to which it belongs, and sum all of these squared
distances.
   ● Print out this sum once each iteration, and you can watch the objective function
converge. Make sure you are picking enough iterations to allow the algorithm to
converge. If the value of the objective function gets worse, then you either have a bug
in your k-means algorithm or a bug in your objective function calculation (or both!).
Thus, explicitly calculating the objective function also serves to test your code. We call
this a “sanity check”.

   There are three provided datasets: data1953.csv, data2008.csv, and dataBoth.csv. The
first two contain 197 countries, with Life Expectancy and Birth Rate measured for each
country, but the first has these measurements taken from 1953, and the second from
2008. dataBoth. csv contains both the 2008 values and the 1953 values, but
pretending that the countries from different years are different countries. Thus, we can
see, for example, that (1953)Zimbabwe falls in the same cluster as (2008)Zimbabwe,
but that (1953)Botswana and (2008)Botswana fall into different clusters.

'''


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import warnings

def function():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    function()

def KMeansClustering(data, k = 2):
    # to get the dimension of the feature space
    rows, cols = data.shape
    
    # Choosing random centers to begin with
    mean = np.mean(data, axis = 0)
    std = np.std(data, axis = 0)
    centers_random = np.random.randn(k, cols)* std + mean
    
    # to initialize array to hold cluster index and distances for each row
    clusters = np.zeros(rows)
    distances = np.zeros((rows, k))
    
    centers_old = np.zeros((k, cols))
    centers_new = centers_random
    
    # Calculating the difference in old and new center
    error = np.linalg.norm(centers_new - centers_old)
    
    # Run till the center stops changing
    while error != 0:
        # get distance of each observation from each center
        for i in range(k):
            distances[:,i] = np.linalg.norm(data - centers_new[i,:], axis = 1)

        # Assign closest cluster
        clusters = np.argmin(distances, axis = 1)

        # Update cluster
        centers_old = centers_new
        centers_new = np.zeros((k, cols))

        for i in range(k):
            centers_new[i,:] = np.mean(data[clusters == i,:], axis=0)

        # Calculate difference
        error = np.linalg.norm(centers_new - centers_old)

    # Return centers and clusters
    return centers_new, clusters
    
if __name__ == "__main__":
    # setting 0 for no annotation,
    # setting to 1 - for annotation with index,
    # 2 - annotation with country name
    annotate = 1
    
    # Read data file
    datafile = input("Data File: ")
    data = pd.read_csv(datafile)
    
    # extract the county names
    countries = data.iloc[:,0].values
    
    # Extract the feature column
    X = np.asarray(data.iloc[:,1:3].values)
    
    # asking the user to enter the number of clusters
    k = int(input("Enter number of clusters (k): "))

    # to get centers and clusters from the K Means Clustering algorithm
    centers, clusters = KMeansClustering(X, k)
    print("Clusters: \n", clusters)
    
    # plot the clusters
    fig, ax = plt.subplots()
    color = iter(plt.cm.rainbow(np.linspace(0,1,k)))
    for i in range(k):
        indexes = np.nonzero(clusters == i)
        ax.scatter(X[indexes,0], X[indexes,1], color = next(color))
        for j in indexes[0]:
            if annotate == 1:
                ax.annotate(str(j), (X[j,0], X[j,1]))
                print(j, "=>", countries[j])
            elif annotate == 2:
                ax.annotate(countries[j], (X[j,0],X[j,1]))
    
    # Label figure
    plt.xlabel("Brith Rate")
    plt.ylabel("Life Expectancy")
    plt.title(datafile)
    plt.show()
    #print(clusters)
    
