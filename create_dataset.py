# %%
import pandas as pd
from sklearn.datasets import load_iris

# %%
iris_data = load_iris()
type(iris_data.data)

# %%
data = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
print(data.head())
target = pd.DataFrame(iris_data.target, columns=['class'])
print(target.head())

# %%
final_dataset = pd.concat([data, target], axis=1)
print(final_dataset.head())

# %%
final_dataset.to_csv("dataset/iris.csv", index=False)

# %%



