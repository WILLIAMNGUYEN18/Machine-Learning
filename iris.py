import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()
#2D PCA
X_reduced = PCA(n_components=2).fit_transform(iris.data)

NEW_reduced = PCA(n_components=1).fit_transform(iris.data)

samplevec = 0
size = (samplevec, ) * 150
#>>> width = 4
#>>> (width,) * 5
#(4, 4, 4, 4, 4)

y = iris.target

"""
For
plt.scatter(X_reduced[: , 0], X_reduced[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
"""
X = iris.data[:, :2]  # we only take the first two features.
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
#print(len(NEW_reduced))
plt.scatter(NEW_reduced[: , 0], size, c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.show()