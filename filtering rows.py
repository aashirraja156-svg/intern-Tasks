import pandas as pd

data = {"Name": ["Ali", "Sara", "Ahmed"],
        "Salary": [50000, 60000, 45000]}

df = pd.DataFrame(data)
print("Original:\n", df, "\n")

# Sort by salary (descending)
df_sorted = df.sort_values(by="Salary", ascending=False)
print("Sorted by Salary:\n", df_sorted)
