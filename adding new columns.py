import pandas as pd

data = {"Name": ["Ali", "Sara", "Ahmed"],
        "Age": [25, 30, 22]}

df = pd.DataFrame(data)

# Add new column for Age after 5 years
df["Age_After_5"] = df["Age"] + 5

print("With New Column:\n", df)
