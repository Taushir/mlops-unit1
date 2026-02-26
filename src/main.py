import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print("First 5 Rows:")
print(df.head())

print("\nBasic Statistics:")
print(df.describe())

print("\nDataset Shape:")
print(df.shape)