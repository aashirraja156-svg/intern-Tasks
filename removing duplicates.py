import pandas as pd

data = {"Name": ["Ali", "Sara", "Ahmed"],
        "Age": [25, 30, 22]}

df = pd.DataFrame(data)
print("Original:\n", df, "\n")

# Filter people older than 23
print("Filtered (Age > 23):\n", df[df["Age"] > 23])
