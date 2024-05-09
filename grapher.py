import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]  # Numerical positions for the bars
labels = ['500,000', '1,000,000', '5,000,000', '10,000,000']  # Labels for the x-axis
y = [45.07, 59.05, 194.36, 339.07]  # Your original data
y2 = [37.10, 40.09,98.72, 161.70]  # Some slightly different data for the second plot

# Create a figure with 1 row and 2 columns of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# First subplot
ax1.bar(x, y, tick_label=labels, color='blue')
ax1.set_xlabel('Number of datapoints')
ax1.set_ylabel('Time')
ax1.set_title('Time of Insert in AVL TREE')

# Second subplot
ax2.bar(x, y2, tick_label=labels, color='green')
ax2.set_xlabel('Number of datapoints')
ax2.set_ylabel('Time')
ax2.set_title('Time of Insert in RED-Black TREE')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the graph
plt.show()
