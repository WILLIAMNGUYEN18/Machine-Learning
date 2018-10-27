import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets


x = np.random.rand(100)
y = x + 0.1*np.random.rand(100)-0.05
prin_comp = PCA(n_components=1).fit_transform((x,y))

print(prin_comp)
plt.scatter(x,y)
plt.plot(prin_comp)
plt.show()