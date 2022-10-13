

import pandas as pd

# winemag_data = pd.read_csv('winemag-data-130k-v2.csv')
# print(winemag_data.sort_values('country'))

# winemag_data = pd.read_csv('winemag-data-130k-v2.csv')
# print(winemag_data.sort_values('country', ascending=False))


winemag_data = pd.read_csv('winemag-data-130k-v2.csv')
print(winemag_data.sort_values(by=['country', 'price']))