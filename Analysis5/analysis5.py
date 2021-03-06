# -*- coding: utf-8 -*-
"""Analysis5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p-BKp8pgpV0KnRZhwpLafkCosssiJ3M1

**Analysis 5**

Clustering
"""

# Commented out IPython magic to ensure Python compatibility.
# imports
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 40)
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
# %matplotlib inline
sns.set_style('darkgrid')
import plotly.express as px
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore');

df = pd.read_csv("CARSSSS.csv")
# to display the top 5 rows
df.head(5)

df.tail(5)

"""Checking the type of data"""

df.dtypes

"""Dropping the duplicate rows"""

duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

"""
Now lets remove the duplicate data because its ok to remove them"""

df.count()   #used to count the number of rows

df = df.drop_duplicates()
df.head(5)

df.count()

"""Dropping the missing or null values"""

print(df.isnull().sum())

df = df.dropna()    # Dropping the missing values.
df.count()

print(df.isnull().sum())   # After dropping the values

"""Converting the object values to integer type.

While having a look at the data, the Price was stored as an object type. This is a serious problem because it is impossible to plot those values on a graph because it is a primary requirement that during plotting a graph all the values must be of type integer data. The author has stored, the Price in a different format (Rs2,34,000) so I had to remove the formatting and then convert them to an integer.
"""

# Removing the formatting
df['Price'] = df['Price'].astype(str)
df['Price'] = [x.replace('Rs',' ') for x in df['Price']]
df['Price'] = [x.replace(',', '') for x in df['Price']]

df['Price']=pd.to_numeric(df['Price'],errors='coerce')

"""**Clustering**

The type of clustering used here is k-means clustering k-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells. k-means clustering minimizes within-cluster variances (squared Euclidean distances)
"""

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

"""Creating some Data"""

from sklearn.datasets import make_blobs

# Create Data
data = make_blobs(n_samples=200, n_features=2, 
centers=4, cluster_std=1.8,random_state=101)

"""Visualize Data"""

plt.scatter(data[0][:,0],data[0][:,1],c=data[1])

plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')

"""Creating the Clusters"""

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4)

kmeans.fit(data[0])

kmeans.cluster_centers_

kmeans.labels_

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))
ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1],c=kmeans.labels_,cmap='rainbow')
ax2.set_title("Original")
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')

"""Now we check some scatter plots but with adding cluster.

But yet we can see that clusters speration in power is stronger than mileage which almost have no separation of clusters

Fuel tank capacity vs Cylinders
"""

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Fuel_Tank_Capacity', y='Cylinders',s=120,palette='viridis')
plt.legend(ncol=4)
plt.title('Scatter plot of Fuel tank capacity and Cylinders with clusters', fontsize=18);
plt.xlabel('Fuel_Tank_Capacity ',fontsize=16)
plt.ylabel('Cylinders',fontsize=16);

"""Now we make an interactive 3D scatter plot of Price,power, and Fuel tank capacity using also clusters"""

fig = px.scatter_3d(df, x='Power', z='Price', y='Fuel_Tank_Capacity',
                    height=700, width=800,color_discrete_sequence=sns.color_palette('colorblind',n_colors=8,desat=1).as_hex(),
                   title='Price Power, and Fuel_Tank_Capacity')
fig.show()