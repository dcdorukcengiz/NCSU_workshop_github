import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78]
}
df = pd.DataFrame(data)

# Plot the data
plt.bar(df['Category'], df['Values'], color='skyblue')
plt.title('Sample Bar Chart')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()