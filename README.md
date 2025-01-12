# Employee Retention Dashboard

## 📊 Project Overview
This project focuses on **employee retention analysis** through data-driven insights and predictive modeling. Using machine learning techniques, we predict the likelihood of employee attrition and identify key factors contributing to employee retention. The ultimate goal is to provide actionable insights to organizations and enhance their people analytics strategy.

## 🚀 Key Features
- **Data Preprocessing**: Includes handling missing values, encoding categorical variables, and addressing class imbalance using SMOTE.
- **Predictive Modeling**: Implements a Random Forest model with hyperparameter tuning for optimal performance.
- **Model Evaluation**: Metrics include Accuracy, ROC-AUC, Classification Report, and Confusion Matrix.
- **Visualizations**: Data visualizations and insights provided through Jupyter Notebooks and will soon include an interactive dashboard.
- **Future Enhancements**:
  - Deployment of an interactive **employee retention dashboard** for real-time analysis.

## 📁 Project Structure
```
.
├── data/                # Contains datasets used for training and evaluation
├── notebooks/           # Jupyter notebooks for exploratory data analysis and modeling
├── scripts/             # Python scripts for data preprocessing and modeling
├── visuals/             # Visualizations generated from the analysis
├── README.md            # Project documentation
└── .gitignore           # Files and directories to ignore in version control
```

## 📂 Directories
### 1. `data/`
Contains raw and processed datasets for analysis. Please ensure no sensitive data is included.

### 2. `notebooks/`
Jupyter Notebooks for:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training and Evaluation

### 3. `scripts/`
Python scripts for modular and reusable code:
- Data Preprocessing
- Model Training
- Evaluation Metrics

### 4. `visuals/`
Generated plots and images to support data insights and model evaluation.

---

## 📊 Results
### Model Performance:
- **Test Accuracy**: 94%
- **ROC-AUC Score**: 0.98
- **Confusion Matrix**:
  ```
  [[352  18]
   [ 30 340]]
  ```

### Key Insights:
- The model demonstrates a strong ability to differentiate between employees likely to leave and stay.
- Key contributing factors to attrition will be visualized in the upcoming dashboard.

---

## ⚙️ Setup and Usage
### Prerequisites
- Python 3.8+
- Required libraries:
  ```bash
  pandas
  numpy
  matplotlib
  seaborn
  scikit-learn
  imbalanced-learn
  ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/PixelQuinn/employee-retention-dashboard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd employee-retention-dashboard
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
1. **Data Analysis**:
   - Open Jupyter Notebooks in the `notebooks/` directory to explore data and model development.
2. **Scripts**:
   - Execute preprocessing and modeling scripts in the `scripts/` directory.
3. **Dashboard** *(Coming Soon)*:
   - A real-time interactive dashboard will be deployed for user-friendly analysis.

---

## 📌 Future Work
- Deployment of an **interactive dashboard** for employee retention analysis.
- Integration of additional machine learning models for benchmarking.
- Incorporating real-world organizational datasets for improved applicability.

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments
- **Libraries Used**:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `imbalanced-learn`.
- Inspiration drawn from employee attrition studies and people analytics best practices.

---

## 📬 Contact
For questions or collaboration, feel free to contact me:
- **GitHub**: [PixelQuinn](https://github.com/PixelQuinn)