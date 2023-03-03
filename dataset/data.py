import pandas as pd

data = pd.read_csv('D:/Tracker/dataset/Ecommerce Purchases.csv')
# print(data)

# data.head(10)
# print( data.tail(10))

# print(data.isnull().sum())

# print(len(data.columns))

print(data['Purchase Price'].mean())