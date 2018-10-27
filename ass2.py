import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np


#https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html

# generate 1000 randomly distributed data points with x and y two features/dimensions 
data = np.random.uniform(-3, 3, size = (1000, 2))
print(data)

#reducing feature to 1,
reduced = PCA(n_components=1).fit_transform(data)


samplevec = 0
size = (samplevec, ) * 1000

plt.scatter(data[: , 0], data[:,1])
plt.show()

plt.clf

#projecting datapoints onto first principal component
plt.scatter(reduced[: , 0], size)
plt.show()

plt.clf


#Reconstruction original points from one principal component
plt.scatter(reduced[: , 0], reduced.T)

plt.show()

