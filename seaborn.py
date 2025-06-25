import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Create synthetic data
np.random.seed(42)
area = np.linspace(500, 3000, 100)  # 100 evenly spaced values between 500 and 3000 sq. ft
price = area * 120 + np.random.normal(0, 20000, 100)  # Price = area × 120 + noise

# Step 2: Create DataFrame
df = pd.DataFrame({
    'Area (sq.ft)': area,
    'Price ($)': price
})

# Step 3: Plot using Seaborn
sns.set(style="whitegrid")
sns.regplot(x='Area (sq.ft)', y='Price ($)', data=df)

plt.title("House Price vs. Area")
plt.xlabel("Area (sq.ft)")
plt.ylabel("Price ($)")
plt.show()
