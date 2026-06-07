# 🏥 Interactive Diabetes Risk Prediction System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📋 Project Overview

A complete end-to-end machine learning system that predicts diabetes risk from patient health information. This project uses the **Pima Indians Diabetes Dataset** and implements multiple ML algorithms to provide accurate, explainable predictions with an interactive user interface.

## ✨ Features

- **🔍 Comprehensive Data Analysis**: Complete EDA with professional visualizations
- **🤖 Multiple ML Models**: Logistic Regression, Decision Tree, Random Forest, KNN
- **📊 Model Comparison**: Automatic selection of best-performing model
- **🎯 Feature Importance**: Understand which health indicators matter most
- **💻 Interactive Prediction**: User-friendly interface for real-time predictions
- **📈 Risk Meter**: Visual risk categorization (Low/Moderate/High)
- **📋 Patient Report**: Comprehensive health assessment with recommendations

## 🎯 Project Objectives

1. Build a beginner-friendly yet professional ML application
2. Implement data preprocessing with median imputation for invalid values
3. Train and compare multiple classification models
4. Provide explainable AI through feature importance analysis
5. Create an interactive prediction system with risk assessment
6. Generate patient reports with personalized recommendations

## 📊 Dataset Information

**Dataset:** Pima Indians Diabetes Dataset  
**Features:** 8 health indicators  
**Target:** Outcome (0 = Non-Diabetic, 1 = Diabetic)

### Input Features:
- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration (mg/dL)
- **Blood Pressure**: Diastolic blood pressure (mm Hg)
- **Skin Thickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)²)
- **Diabetes Pedigree Function**: Genetic predisposition score
- **Age**: Age in years


## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Verify dataset file:**
   - Ensure `Book1.csv` is in the project directory

### Running the Application

**Option 1: Python Script**
```bash
python diabetes_prediction_system.py
```

**Option 2: Jupyter Notebook**
```bash
jupyter notebook Diabetes_Prediction_System.ipynb
```

**Option 3: Google Colab**
- Upload `Diabetes_Prediction_System.ipynb` to Google Colab
- Upload `Book1.csv` to the Colab environment
- Run all cells

## 📁 Project Structure

```
Task 1 Diabetes prediction using ML/
│
├── Book1.csv                           # Original dataset
├── diabetes_prediction_system.py       # Main Python script
├── Diabetes_Prediction_System.ipynb    # Jupyter Notebook
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── DEMO_SCRIPT.md                     # 3-minute demo script
├── LINKEDIN_POST.md                   # LinkedIn project description
│
└── Generated Files (after running):
    ├── diabetes_cleaned.csv            # Cleaned dataset
    ├── EDA_Visualizations.png          # Exploratory analysis charts
    ├── Model_Comparison.png            # Model performance comparison
    ├── Feature_Importance.png          # Feature ranking chart
    └── model_comparison.csv            # Performance metrics table
```

## 🔬 Methodology

### 1. Data Preprocessing
- Load and explore the dataset
- Identify and handle invalid zero values
- Apply median imputation for missing data
- Create cleaned dataset

### 2. Exploratory Data Analysis
- Class distribution visualization
- Correlation heatmap analysis
- Feature distribution plots
- Diabetic vs Non-diabetic comparison

### 3. Model Training
- Train 4 classification models
- Evaluate using Accuracy, Precision, Recall, F1 Score
- Automatically select best-performing model
- Prioritize Random Forest for optimal performance

### 4. Feature Importance
- Identify most influential health indicators
- Rank features by predictive power
- Visualize feature contributions

### 5. Interactive Prediction
- Collect patient health information
- Generate real-time risk predictions
- Display visual risk meter
- Provide comprehensive patient report


## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | ~77% | ~75% | ~66% | ~70% |
| Decision Tree | ~72% | ~67% | ~65% | ~66% |
| **Random Forest** | **~78%** | **~76%** | **~68%** | **~72%** |
| KNN | ~75% | ~72% | ~64% | ~68% |

*Note: Actual performance may vary slightly due to random state*

## 🎯 Risk Categories

| Probability | Risk Level | Recommendation |
|-------------|------------|----------------|
| < 30% | 🟢 Low Risk | Maintain healthy lifestyle |
| 30% - 70% | 🟡 Moderate Risk | Monitor regularly, lifestyle modifications |
| > 70% | 🔴 High Risk | Consult healthcare professional immediately |

## 💡 Key Insights

- **Glucose level** is typically the strongest predictor of diabetes
- **BMI** and **Age** are significant contributing factors
- **Diabetes Pedigree Function** indicates genetic predisposition
- Early detection enables better health management

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ End-to-end ML workflow implementation
- ✅ Data preprocessing and cleaning techniques
- ✅ Multiple model training and comparison
- ✅ Feature engineering and importance analysis
- ✅ Model evaluation with multiple metrics
- ✅ Interactive system development
- ✅ Professional visualization creation
- ✅ Explainable AI principles

## 🛠️ Technologies Used

- **Programming Language:** Python 3.8+
- **ML Framework:** Scikit-Learn
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Development Environment:** Jupyter Notebook, VS Code

## 📝 Sample Prediction

```
Pregnancies: 6
Glucose: 148 mg/dL
Blood Pressure: 72 mm Hg
Skin Thickness: 35 mm
Insulin: 125 mu U/ml
BMI: 33.6
Diabetes Pedigree Function: 0.627
Age: 50 years

RESULT:
████████████████░░░░  🔴 HIGH RISK
Risk Probability: 82.3%
Prediction: DIABETIC
```

## 🤝 Contributing

This is an internship project. Feedback and suggestions are welcome!

## 📧 Contact

For questions or feedback about this project:
- **Platform:** InternPE Internship
- **Project:** Task 1 - Diabetes Prediction using ML

## 📄 License

This project is created for educational purposes as part of an internship program.

## 🙏 Acknowledgments

- Pima Indians Diabetes Dataset
- Scikit-Learn Documentation
- InternPE Internship Program

---

**⭐ If you found this project helpful, please star this repository!**

*Built with ❤️ for learning and innovation*
