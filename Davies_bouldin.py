import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score,silhouette_score,silhouette_samples
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt

from sklearn import datasets
iris = datasets.load_iris()


import warnings
warnings.filterwarnings("ignore")
#%matplotlib inline

df=pd.DataFrame(iris['data'])
print(df.head())




def get_kmeans_score(data, center):
    
    
    kmeans = KMeans(n_clusters=center)

    model = kmeans.fit_predict(df)
    
    
    score = davies_bouldin_score(df, model)
    
    return score
scores = []
centers = list(range(2,30))
for center in centers:
    scores.append(get_kmeans_score(df, center))




plt.plot(centers, scores, linestyle='--', marker='o', color='b');
plt.xlabel('K');
plt.ylabel('Davies Bouldin score');
plt.title('Davies Bouldin score vs. K');
