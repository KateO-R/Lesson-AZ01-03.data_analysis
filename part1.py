import pandas as pd

df = pd.read_csv('animal.csv')

print(df)

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)