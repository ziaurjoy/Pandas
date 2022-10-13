
import pandas as pd

# read_csv = pd.read_csv('data.csv')
# print(read_csv.shape)


# read_csv = pd.read_csv('data.csv')
# print(read_csv.head())

read_csv = pd.read_csv('data.csv', index_col=3)
print(read_csv.head())