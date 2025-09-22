import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = pd.DataFrame({
    "Category": ["A", "B", "C", "A", "B", "C"],
    "Values": [4, 7, 2, 8, 6, 5]
})

# Bar Plot
sns.barplot(x="Category", y="Values", data=data)
plt.title("Bar Plot with Seaborn")
plt.show()

# Scatter Plot with regression line
sns.lmplot(x="Category", y="Values", data=data, fit_reg=True)
plt.show()
