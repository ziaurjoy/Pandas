import pandas as pd


# winemag_data = pd.read_csv('winemag-data-130k-v2.csv')
# point = winemag_data.points
# result =  point.map(lambda p: p-2)
# print(result)



winemag_data = pd.read_csv('winemag-data-130k-v2.csv')
point = winemag_data.points
result =  point.map(lambda p: winemag_data.country)
print(result)