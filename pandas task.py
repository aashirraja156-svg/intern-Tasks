import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "Department": ["HR", "IT", "Finance", "IT"]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Inspect data
print(df.head())   # first 5 rows
print(df.info())   # summary
print(df.describe())  # stats

# Select column
print("Names:", df["Name"])

# Filter rows
print("Age > 25:\n", df[df["Age"] > 25])

# Group by
grouped = df.groupby("Department")["Age"].mean()
print("Average Age by Department:\n", grouped)

# Add new column
df["Age+5"] = df["Age"] + 5
print(df)
