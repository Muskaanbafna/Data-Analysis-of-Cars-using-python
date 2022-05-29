# -*- coding: utf-8 -*-
"""Analysis1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W34t5MZGSoE6t96fu88ORavsI4PdKwJk

**Analysis 1**

**Some general analysis encountered during Data Cleaning**
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

"""**Checking the type of data**

"""

df.dtypes

"""**Dropping the duplicate rows**"""

duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

"""**Now lets remove the duplicate data because its ok to remove them**"""

df.count()   #used to count the number of rows

df = df.drop_duplicates()
df.head(5)

df.count()

"""**Dropping the missing or null values**"""

print(df.isnull().sum())

df = df.dropna()    # Dropping the missing values.
df.count()

print(df.isnull().sum())   # After dropping the values