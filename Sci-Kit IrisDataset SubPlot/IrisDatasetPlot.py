# ============ Data Science, Algorithms and Advanced Software Engineering ===============
# ============ Johnson Temilola - [2019/07/01] ===========
'''
   Creating the 12 subplots Iris dataset
'''

import matplotlib.pyplot as plt
from sklearn import datasets

# load the iris dataset
iris = datasets.load_iris()

# mapping the different species to different colors
colors = ["r", "b", "g"]
colors = list(map(lambda x: colors[x], iris["target"]))

# Creating 12 subplots
f, axes = plt.subplots(4, 3)
row = 0
for i in range(4):
    col = 0
    for j in range(4):
        if i != j:
            # Make Scatter Plot of i-th column with j-th column only when i is not equal to j (i != j)
            axes[row,col].scatter(iris["data"][:,i],iris["data"][:,j], c = colors, edgecolors = "k", s = 15)
            col += 1
    row += 1

# saving and show the figure
plt.savefig("irisDataset.png")
plt.show()
