
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np


#https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html

# generate 1000 randomly distributed data points with x and y two features/dimensions 

#adjusted automatically to be centered on 0 by limiting between -3, 3
data = np.random.uniform(-3, 3, size = (1000, 2))
print(data)

reduced = PCA(n_components=1).fit_transform(data)
print(reduced)
pca = PCA(n_components=1)
pca.fit(data)
print (pca.components_)
print(type(pca.components_))
print(pca.components_[0,0])
print(pca.components_[0,1])

scalar = [pca.components_[0,0],pca.components_[0,1],pca.components_[0,0] * 5,pca.components_[0,1] * 5]
x = [pca.components_[0,0], pca.components_[0,0] * 5]
y = [pca.components_[0,1], pca.components_[0,1] * 5]
print(scalar)
#print(scalar[0,0])
#print(scalar[0,1])
#print(scalar[0,2])
#print(scalar[0,3])
plt.scatter(reduced[:,0],y)
plt.plot(x,y)
plt.show()
#plt.scatter(reduced[:,0], reduced[:,1])
#plt.plot(pca.components_)
#plt.scatter(data[])
#plt.show()

# calculate the first principle component and project the datapoints onto it

# reconstruct the original points from this one principal component
