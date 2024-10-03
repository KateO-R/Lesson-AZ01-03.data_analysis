import pandas as pd
import matplotlib.pyplot as plt

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Ann', 'Andrew', 'Jack', 'Helene', 'Kate'],
    'notes_math': [5, 1, 4, 5, 4, 3, 5, 5, 4, 5],
    'notes_Eng': [5, 4, 3, 4, 5, 3, 4, 4, 5, 5],
    'notes_statistics': [5, 3, 5, 3, 4, 3, 3, 4, 5, 5],
    'notes_chemistry': [5, 4, 3, 4, 5, 3, 4, 4, 5, 5],
    'notes_arts': [5, 4, 4, 5, 5, 5, 5, 4, 5, 5],
}

df = pd.DataFrame(data)

print(df.head(5))
print(f'Median Math note - {df['notes_math'].median()}')
print(f'Median English note - {df['notes_Eng'].median()}')
print(f'Median Statistics note - {df['notes_statistics'].median()}')
print(f'Median Chemistry note - {df['notes_chemistry'].median()}')
print(f'Median Arts note - {df['notes_arts'].median()}')

print(f'Standard deviation of Math notes - {df['notes_math'].std()}')

df.boxplot(column='notes_math')
plt.show()

Q1_math = df['notes_math'].quantile(0.25)
Q3_math = df['notes_math'].quantile(0.75)
IQR = Q3_math-Q1_math
