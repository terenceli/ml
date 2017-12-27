from sklearn.preprocessing import Imputer
import numpy as np
from sklearn.decomposition import PCA

data = np.loadtxt("secom.data")
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(data)
data = imp.transform(data)

pca = PCA(n_components=6)

pca.fit(data)
print (pca.explained_variance_ratio_)
print (pca.singular_values_)
print (np.shape(pca.components_))
