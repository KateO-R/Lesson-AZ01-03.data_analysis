import pandas as pd

df = pd.read_csv('dz.csv')
df.fillna(0, inplace=True)
group = df.groupby('City')['Salary'].mean().round(2)

print(group)
