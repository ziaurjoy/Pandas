import pandas as pd


# winemag_data = pd.read_csv('winemag-data-130k-v2.csv')
# print(winemag_data[pd.isnull(winemag_data.country)])


# winemag_data = pd.read_csv('winemag-data-130k-v2.csv')
# print(winemag_data.country.fillna('Bangladesh'))


winemag_data = pd.read_csv('winemag-data-130k-v2.csv')
print(winemag_data.country.replace('US', 'United America'))

