import pandas as pd

data = {"City": ["Lahore", "Karachi", "Lahore", "Karachi"],
        "Salary": [50000, 60000, 55000, 65000]}

df = pd.DataFrame(data)
print("Original:\n", df, "\n")

# Group by city and take average salary
avg_salary = df.groupby("City")["Salary"].mean()
print("Average Salary by City:\n", avg_salary)