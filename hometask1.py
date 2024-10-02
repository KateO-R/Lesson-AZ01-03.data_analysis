import pandas as pd

df = pd.read_csv('global_income_inequality.csv')

print(df.head(5))
print(df.info())
print(df.describe())