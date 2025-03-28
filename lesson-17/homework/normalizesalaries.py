import pandas as pd
# Load employee dataset
df_employees = pd.read_csv('employee.csv')

# Normalize salaries within each department
df_employees['NormalizedSalary'] = df_employees.groupby('DEPARTMENT')['BASE_SALARY'].transform(
    lambda x: (x - x.mean()) / x.std()
)

print(df_employees.head(10))