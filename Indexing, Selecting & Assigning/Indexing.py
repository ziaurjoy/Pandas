
import pandas as pd


# read_csv = pd.read_csv('data.csv')
# print(read_csv)


# read_csv = pd.read_csv('data.csv')
# print(read_csv.country)

# read_csv = pd.read_csv('data.csv')
# print(read_csv['country'])


# read_csv = pd.read_csv('data.csv')
# print(read_csv['country'][0])



# INDEX BASED SELECTION(iloc)

# read_csv = pd.read_csv('data.csv')
# print(read_csv.iloc[0])


# read_csv = pd.read_csv('data.csv')
# print(read_csv.iloc[:, 1])

# read_csv = pd.read_csv('data.csv')
# print(read_csv.iloc[:3, 1])


# read_csv = pd.read_csv('data.csv')
# print(read_csv.iloc[2:3, 1])


# read_csv = pd.read_csv('data.csv')
# print(read_csv.iloc[[1, 5, 9, 10], [1, 4, 5, 8]])


# read_csv = pd.read_csv('data.csv')
# print(read_csv.iloc[-5:, [1, 4, 5, 8]])






# LEVEL BASED SELECTION

# read_csv = pd.read_csv('data.csv')
# print(read_csv.loc[0])


# read_csv = pd.read_csv('data.csv')
# print(read_csv.loc[:, ['country', 'description', 'designation', 'price']])

# read_csv = pd.read_csv('data.csv')
# print(read_csv.set_index('country'))



# read_csv = pd.read_csv('data.csv')
# print(read_csv.country == 'Italy')


# read_csv = pd.read_csv('data.csv')
# print(read_csv.loc[(read_csv.country == 'Italy') & (read_csv.variety == 'Sangiovese')])


# read_csv = pd.read_csv('data.csv')
# print(read_csv.loc[read_csv.country.isin(['Italy', 'France'])])


# read_csv = pd.read_csv('data.csv')
# print(read_csv.loc[read_csv.price.notnull()])



# Assigning data

# read_csv = pd.read_csv('data.csv')
# read_csv['critic'] = 'everyone Joy'
# print(read_csv.loc[:, 'critic'])


read_csv = pd.read_csv('data.csv')
read_csv['index_backwards'] = range(len(read_csv), 0, -1)
print(read_csv.loc[:, 'index_backwards'])




