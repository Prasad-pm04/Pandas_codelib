import matplotlib.pyplot as plt

# Data to plot
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 30, 20, 25]  # Percentages
colors = ['red', 'yellow', 'pink', 'brown']
explode = (0, 0.1, 0, 0)  # "explode" the 2nd slice (Bananas)

# Create the pie chart
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Fruit Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is a circle.

# Show the chart
plt.show()
