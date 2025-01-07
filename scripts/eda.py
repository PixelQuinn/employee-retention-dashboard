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

# The Attrition Distribution graph highlights a significant class imbalance in the dataset. 
# Approximately 1200 employees have not left the company (labeled as "No"), while only about 240 employees have left (labeled as "Yes"). 
# This translates to roughly an 83% to 17% split between retained and departed employees. 
# Such an imbalance may lead to predictive models favoring the majority class ("No") and failing to identify employees at risk of leaving. 
# To address this, we will explore techniques such as oversampling, undersampling, or class weights, along with evaluation metrics like precision, recall, and F1-score, 
# ensuring the model captures meaningful patterns related to attrition.

# Attrition proportions to check data balance
attrition_count = data['Attrition'].value_counts(normalize=True)
print("\nAttrition Proportions:")
print(attrition_count)

# Turnover by Department
sns.countplot(x='Department', hue='Attrition', data=data)
plt.title('Attrition by Department')
plt.xticks(rotation=45)
plt.show()

# EDA Analysis: Employee Attrition
# --------------------------------

# 1. Overall Attrition Distribution
# - Class Imbalance Observed:
#   * Retained Employees: ~1200 (83%).
#   * Departures: ~240 (17%).
# - Key Implications:
#   * Imbalance may lead to poor predictions for the minority class (departures).
#   * Mitigation Strategies:
#     - Resampling techniques (e.g., SMOTE, undersampling).
#     - Assigning class weights in models.
#   * Model Evaluation Focus:
#     - Emphasize metrics like precision, recall, and F1-score to ensure fair assessment.

# 2. Departmental Attrition Analysis
# Research & Development (R&D):
# - Largest Workforce: ~950 employees.
# - Departures: 133 (14% attrition rate).
# - Key Insight:
#   * Highest absolute turnover, but proportional attrition rate appears stable for its size.

# Sales:
# - Mid-Sized Workforce: ~430 employees.
# - Departures: 90 (21% attrition rate).
# - Key Insight:
#   * Highest proportional attrition, indicating potential challenges in retention related to workload, compensation, or satisfaction.

# Human Resources (HR):
# - Smallest Workforce: ~60 employees.
# - Departures: 7 (12% attrition rate).
# - Key Insight:
#   * Lowest absolute turnover and a stable retention rate, potentially reflecting strong internal policies.

# 3. Key Insights:
# - Sales Department:
#   * High proportional attrition requires investigation into drivers such as workload, pay structure, and career growth opportunities.
# - R&D Department:
#   * Largest department with stable proportional attrition, though absolute losses warrant monitoring.
# - HR Department:
#   * Low turnover and stable retention, suggesting effective HR practices that may be modeled across other departments.

# 4. Next Steps:
# - Feature Exploration:
#   * Analyze age, salary, job satisfaction, work-life balance, and tenure as potential attrition drivers.
# - Class Imbalance Handling:
#   * Implement techniques like SMOTE, undersampling, or class weighting during modeling.
# - Evaluation Metrics:
#   * Focus on precision, recall, and F1-score to ensure balanced performance across classes.
# - Department-Specific Strategies:
#   * Investigate retention challenges in Sales and monitor trends in R&D for targeted interventions.

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
# ------------------------
# 1. Attrition Trends by Age:
# - Peak attrition observed in younger age groups (28-35).
# - Employee distribution concentrated in the 30-40 age range.

# 2. Key Observations:
# - Younger employees (25-35) show **higher attrition rates**, possibly due to:
#   * Early career exploration.
#   * Desire for faster growth or dissatisfaction with pay.
# - Mid-career employees (35-45) have **moderate attrition**, suggesting:
#   * Balancing work-life commitments or career plateaus.
# - Senior employees (45+) demonstrate **better retention**, indicating:
#   * Stability in roles and reduced job-switching tendencies.

# 3. Distribution Insights:
# - Age distribution is **roughly normal**:
#   * Mean age falls in the mid-30s.
#   * Fewer employees are observed at the extremes (<25 and >55).
# - Retention improves as age increases, aligning with job security preferences.

# 4. Risk Areas and Recommendations:
# - Younger Workforce (25-35):
#   * Focus retention strategies on growth opportunities, mentorship, and career development programs.
#   * Assess salary competitiveness and job satisfaction metrics.
# - Mid-Career Employees (35-45):
#   * Provide pathways for upskilling, leadership training, and lateral movement.
# - Senior Employees (45+):
#   * Leverage insights from lower attrition rates to create mentoring opportunities and retain organizational knowledge.

# Correlation Heatmap
numeric_features = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_features.corr()

plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title('Correlation Heatmap')
plt.show()