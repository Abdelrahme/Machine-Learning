
import pandas as pd
import numpy as np
import matplotlib.pyplot as pltmatplotlib
from matplotlib import style, pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data=pd.read_csv('data.csv.csv')

#%%

data.isnull().sum()

#%%

#determine the correlation of data
cor_matrix=data.corr()
upper =cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
to_drop=[column for column in upper.columns if any(upper[column]>0.8) or any(upper[column]<-0.8)]
to_drop

#%%

data.info()
from yellowbrick.cluster import KElbowVisualizer
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10), timings = False)
visualizer.fit(data)
visualizer.show()

from sklearn.cluster import KMeans
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(data)
y_predicted


data['cluster']=y_predicted
data.head(10)

print(km.cluster_centers_)

plt.figure(figsize=(10,8))
plt.scatter(data.values[y_predicted==0, 0], data.values[y_predicted==0 ,1],s=100,c='red',label='cluster0')
plt.scatter(data.values[y_predicted==1, 0], data.values[y_predicted==1 ,1],s=100,c='blue',label='cluster1')
plt.scatter(data.values[y_predicted==2, 0], data.values[y_predicted==2 ,1],s=100,c='green',label='cluster2')
plt.scatter(km.cluster_centers_[:, 0],km.cluster_centers_[:,1], s=100,c='yellow',label='centroid')
plt.legend()

