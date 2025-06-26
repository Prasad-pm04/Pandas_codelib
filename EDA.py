# Titanic EDA - Kaggle Dataset
# Dataset link: https://www.kaggle.com/competitions/titanic/data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("train.csv")  # Use full path if needed

# 1. Basic Info
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.info())
print(df.describe())

# 2. Check for null values
print("\nMissing Values:\n", df.isnull().sum())

# 3. Data Cleaning - Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 4. Univariate Analysis - Categorical
sns.countplot(data=df, x='Survived')
plt.title("Survival Count")
plt.show()

sns.countplot(data=df, x='Pclass')
plt.title("Passenger Class Distribution")
plt.show()

# 5. Univariate Analysis - Numerical
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 6. Bivariate Analysis
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title("Age vs Passenger Class")
plt.show()

sns.barplot(x='Sex', y='Survived', data=df)
plt.title("Survival Rate by Gender")
plt.show()

# 7. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
