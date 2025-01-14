# Employee Retention Dashboard

## 📊 Project Overview
This project focuses on **employee retention analysis** through data-driven insights and interactive visualization. Using machine learning techniques, we predict the likelihood of employee attrition and identify key factors contributing to employee retention. The ultimate goal is to provide actionable insights to organizations and enhance their people analytics strategy.

## 🚀 Key Features
- **Data Preprocessing**: Includes handling missing values, encoding categorical variables, and addressing class imbalance using SMOTE.
- **Predictive Modeling**: Implements a Random Forest model with hyperparameter tuning for optimal performance.
- **Model Evaluation**: Metrics include Accuracy, ROC-AUC, Classification Report, and Confusion Matrix.
- **Interactive Dashboard**: A **Tableau dashboard** visualizes key metrics, such as attrition rate, tenure, and monthly income distribution.
- **Data-Driven Insights**: Highlights department-specific attrition rates and key metrics like employee tenure and compensation trends.

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
Contains raw and processed datasets for analysis.

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
- The Tableau dashboard provides a comprehensive overview of retention metrics and department-level analysis.

---

## 🔧 Setup and Usage
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
3. **Dashboard**:
   - The interactive Tableau dashboard can be embedded below (once hosted):

     <div class='tableauPlaceholder' id='viz1736822690743' style='position: relative'><noscript><a href='#'><img alt='Workforce Analytics Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Em&#47;EmployeeAttritionDashboard_17368226388350&#47;WorkforceAnalyticsDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='EmployeeAttritionDashboard_17368226388350&#47;WorkforceAnalyticsDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Em&#47;EmployeeAttritionDashboard_17368226388350&#47;WorkforceAnalyticsDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1736822690743');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1227px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

---

## 📆 Future Work
- Expansion of dashboard features to include predictive insights.
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

## 📢 Contact
For questions or collaboration, feel free to contact me:
- **GitHub**: [PixelQuinn](https://github.com/PixelQuinn)