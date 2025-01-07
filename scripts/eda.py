import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("../data/Employee_data.csv")

# Inspect the first five rows
print("Dataset Preview:")
print(data.head())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Visualize Attrition Distribution
sns.countplot(x='Attrition', data=data)
plt.title('Attrition Distribution')
plt.show()

# Attrition proportions to check data balance
attrition_count = data['Attrition'].value_counts(normalize=True)
print("\nAttrition Proportions:")
print(attrition_count)

# Turnover by Department
sns.countplot(x='Department', hue='Attrition', data=data)
plt.title('Attrition by Department')
plt.xticks(rotation=45)
plt.show()

# Turnover by Age
sns.histplot(data=data, x='Age', hue='Attrition', multiple='stack', bins=20)
plt.title('Attrition by Age')
plt.show()

# Correlation Heatmap
numeric_features = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_features.corr()

plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title('Correlation Heatmap')
plt.show()