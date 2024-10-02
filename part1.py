import pandas as pd

data = {
    'Age': [23, 30, 22, 27, 21, 20, 29, 28, 22, 25],
    'Salary': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000],
}

df = pd.DataFrame(data)

print(f'Average age - {df['Age'].mean()}')
print(f'Median age - {df['Age'].median()}')
print(f'Standard deviation of the age - {df['Age'].std()}')

print(f'Average salary - {df['Salary'].mean()}')
print(f'Median salary - {df['Salary'].median()}')
print(f'Standard deviation of the salary - {df['Salary'].std()}')