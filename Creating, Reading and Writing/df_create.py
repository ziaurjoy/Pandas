

import pandas as pd

# df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
# print(df)

# df = pd.DataFrame({'Bob': ['I like it', 'It was awful'], 'Sue': ['Pretty good', 'Bland']})
# print(df)


# given index in DF

# df = pd.DataFrame({'Bob': ['I liked it', 'It was awful'], 'Sue': ['Pretty good', 'Bland']}, index=['Product A', 'Product B'])
# print(df)




# SERIES
# series = pd.Series([1, 2, 3, 4, 5])
# print(series)


# series = pd.Series([1, 2, 3, 4, 5], index=['Sales A', 'Sales B', 'Sales C', 'Sales D', 'Sales E'])
# print(series)

series = pd.Series([1, 2, 3, 4, 5], index=['Sales A', 'Sales B', 'Sales C', 'Sales D', 'Sales E'], name="Total Sell")
print(series)