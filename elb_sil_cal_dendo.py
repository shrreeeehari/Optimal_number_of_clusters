import pandas as pd

from sklearn.cluster import KMeans


from sklearn import datasets
iris = datasets.load_iris()


import warnings
warnings.filterwarnings("ignore")
#%matplotlib inline

df=pd.DataFrame(iris['data'])
print(df.head())



# Elbow Method for K means ========================================

from yellowbrick.cluster import KElbowVisualizer
model = KMeans()

visualizer = KElbowVisualizer(model, k=(2,30))
visualizer.fit(df)        
visualizer.show()        


# Silhouette Score for K means ====================================
from yellowbrick.cluster import KElbowVisualizer
model = KMeans()

visualizer = KElbowVisualizer(model, k=(2,30),metric='silhouette')
visualizer.fit(df)        
visualizer.show()  


# Calinski Harabasz Score for K means ====================================
from yellowbrick.cluster import KElbowVisualizer
model = KMeans()

visualizer = KElbowVisualizer(model, k=(2,30),metric='calinski_harabasz')
visualizer.fit(df)        
visualizer.show()        



# Dendogram for Heirarchical Clustering ==================================
import scipy.cluster.hierarchy as shc
from matplotlib import pyplot
pyplot.figure(figsize=(10, 7))  
pyplot.title("Dendrograms")  
dend = shc.dendrogram(shc.linkage(df, method='ward'))




