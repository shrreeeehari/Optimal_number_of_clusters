import numpy as np
import pandas as pd

from sklearn.cluster import KMeans


import matplotlib.pyplot as plt


from sklearn import datasets
iris = datasets.load_iris()


import warnings
warnings.filterwarnings("ignore")
#%matplotlib inline

df=pd.DataFrame(iris['data'])
print(df.head())



def optimalK(data, nrefs=3, maxClusters=15):
  
    gaps = np.zeros((len(range(1, maxClusters)),))
    resultsdf = pd.DataFrame({'clusterCount':[], 'gap':[]})
    for gap_index, k in enumerate(range(1, maxClusters)):

        refDisps = np.zeros(nrefs)

        for i in range(nrefs):
            
           
            randomReference = np.random.random_sample(size=data.shape)
            
            
            km = KMeans(k)
            km.fit(randomReference)
            
            refDisp = km.inertia_
            refDisps[i] = refDisp

        km = KMeans(k)
        km.fit(data)
        
        origDisp = km.inertia_

        gap = np.log(np.mean(refDisps)) - np.log(origDisp)

        gaps[gap_index] = gap
        
        resultsdf = resultsdf.append({'clusterCount':k, 'gap':gap}, ignore_index=True)
    return (gaps.argmax() + 1, resultsdf)



score_g, dp = optimalK(df, nrefs=5, maxClusters=20)
plt.plot(dp['clusterCount'], dp['gap'], linestyle='--', marker='o', color='b');
plt.xlabel('K');
plt.ylabel('Gap Statistic');
plt.title('Gap Statistic vs. K');


