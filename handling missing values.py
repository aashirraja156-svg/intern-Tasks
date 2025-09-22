import pandas as pd

data = {"Name": ["Ali", "Sara", "Ahmed", None],
        "Age": [25, None, 30, 28]}

df = pd.DataFrame(data)
print("Original:\n", df, "\n")

# Fill missing age with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Drop rows where Name is missing
df.dropna(subset=["Name"], inplace=True)

print("Cleaned:\n", df)
