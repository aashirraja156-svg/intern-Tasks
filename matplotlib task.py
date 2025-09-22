import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Line Plot
plt.plot(x, y, marker="o", color="blue", label="y = 2x")
plt.title("Line Plot with Matplotlib")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Bar Chart
plt.bar(x, y, color="orange")
plt.title("Bar Chart with Matplotlib")
plt.show()
