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

# EDA Observation: Attrition Distribution
# ----------------------------------------
# - Significant class imbalance observed:
#   * Retained Employees: ~83%.
#   * Departed Employees: ~17%.
# - Key Implication:
#   * Predictive models may favor the majority class ("No").
# - Next Steps:
#   * Address imbalance through resampling techniques (e.g., SMOTE, undersampling).
#   * Use evaluation metrics such as precision, recall, and F1-score for balanced assessment.

# Attrition proportions to check data balance
attrition_count = data['Attrition'].value_counts(normalize=True)
print("\nAttrition Proportions:")
print(attrition_count)

# Turnover by Department
sns.countplot(x='Department', hue='Attrition', data=data)
plt.title('Attrition by Department')
plt.xticks(rotation=45)
plt.show()

# Departmental Attrition Analysis
# --------------------------------
# 1. Research & Development (R&D):
#   - Largest workforce (~950 employees).
#   - Absolute turnover: 133 employees (14% attrition rate).
#   - Key Insight:
#     * Stable proportional attrition, but total losses are the highest.

# 2. Sales:
#   - Mid-sized workforce (~430 employees).
#   - Absolute turnover: 90 employees (21% attrition rate).
#   - Key Insight:
#     * Highest proportional attrition, suggesting potential challenges in workload or satisfaction.

# 3. Human Resources (HR):
#   - Smallest workforce (~60 employees).
#   - Absolute turnover: 7 employees (12% attrition rate).
#   - Key Insight:
#     * Low turnover and stable retention, indicating effective internal policies.

# 4. Recommendations:
#   - Sales:
#     * Investigate drivers like workload, compensation, and career growth opportunities.
#   - R&D:
#     * Monitor attrition trends and ensure retention in key roles.
#   - HR:
#     * Replicate successful practices across other departments.

# Turnover by Age
sns.histplot(data=data, x='Age', hue='Attrition', multiple='stack', bins=20)
plt.title('Attrition by Age')
plt.show()

# Distribution of Age
sns.histplot(data=data, x='Age', bins=15, kde=True, hue='Attrition')
plt.title('Age Distribution with Attrition')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Boxplot of Age by Attrition
sns.boxplot(x='Attrition', y='Age', data=data)
plt.title('Age and Attrition Trends')
plt.show()

attrition_age_stats = data.groupby('Attrition')['Age'].describe()
print(attrition_age_stats)

# Age Distribution Analysis
# --------------------------
# 1. Attrition Trends by Age:
# - Younger employees (25-35) exhibit **higher attrition rates**, likely due to:
#   * Career exploration or dissatisfaction with pay.
#   * Desire for faster growth opportunities.
# - Mid-career employees (35-45) have **moderate attrition**, possibly due to:
#   * Balancing work-life commitments or reaching career plateaus.
# - Senior employees (45+) demonstrate **better retention**, suggesting:
#   * Job stability and reduced inclination to switch roles.

# 2. Statistical Insights:
# - Attrition group (`Yes`) mean age: **33.6 years**.
# - Retention group (`No`) mean age: **37.6 years**.
# - Younger employees dominate the attrition group, while retention improves with age.

# 3. Recommendations:
# - Younger Employees (25-35):
#   * Focus on growth opportunities, mentorship, and career development programs.
#   * Regularly assess job satisfaction and salary competitiveness.
# - Mid-Career Employees (35-45):
#   * Offer leadership training, upskilling programs, and lateral movement opportunities.
# - Senior Employees (45+):
#   * Leverage their stability and organizational knowledge through mentoring initiatives.

# Correlation Heatmap
numeric_features = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_features.corr()

plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title('Correlation Heatmap')
plt.show()

# Correlation Heatmap Insights
# ----------------------------
# - Identify relationships between numerical features and target variable (`Attrition`).
# - Use high-correlation features as predictors in modeling.