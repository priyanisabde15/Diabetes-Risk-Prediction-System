"""
=============================================================================
INTERACTIVE DIABETES RISK PREDICTION SYSTEM
=============================================================================
Project: Machine Learning-based Diabetes Risk Assessment
Dataset: Pima Indians Diabetes Dataset
Author: InternPE Internship Project
Description: A complete end-to-end ML system for predicting diabetes risk
=============================================================================
"""

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

print("="*80)
print(" DIABETES RISK PREDICTION SYSTEM ".center(80, "="))
print("="*80)
print()

# =============================================================================
# PART 1: DATA PREPROCESSING
# =============================================================================
print("\n" + "="*80)
print(" PART 1: DATA PREPROCESSING ".center(80))
print("="*80 + "\n")

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('Book1.csv')
print("✓ Dataset loaded successfully!\n")

# Display basic information
print("Dataset Shape:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

print("Dataset Info:")
print(df.info())
print()

print("Summary Statistics:")
print(df.describe())
print()

print("Missing Values:")
missing_values = df.isnull().sum()
print(missing_values)
if missing_values.sum() == 0:
    print("✓ No missing values found!\n")
else:
    print(f"⚠ Total missing values: {missing_values.sum()}\n")

# Identify columns with invalid zero values
print("Identifying Invalid Zero Values...")
print("-" * 80)
columns_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for column in columns_with_zeros:
    zero_count = (df[column] == 0).sum()
    print(f"{column}: {zero_count} zero values found")

print()

# Replace invalid zeros with median values
print("Replacing Invalid Zeros with Median Values...")
print("-" * 80)

# Create a copy for cleaned data
df_cleaned = df.copy()

for column in columns_with_zeros:
    # Calculate median of non-zero values
    median_value = df_cleaned[df_cleaned[column] != 0][column].median()
    
    # Replace zeros with median
    df_cleaned[column] = df_cleaned[column].replace(0, median_value)
    
    print(f"{column}: Replaced with median = {median_value:.2f}")

print("\n✓ Data cleaning completed successfully!\n")

# Save cleaned dataset
df_cleaned.to_csv('diabetes_cleaned.csv', index=False)
print("✓ Cleaned dataset saved as 'diabetes_cleaned.csv'\n")

# =============================================================================
# PART 2: EXPLORATORY DATA ANALYSIS (EDA)
# =============================================================================
print("\n" + "="*80)
print(" PART 2: EXPLORATORY DATA ANALYSIS ".center(80))
print("="*80 + "\n")

# 1. Class Distribution
print("Generating visualizations...\n")

plt.figure(figsize=(12, 10))

# Plot 1: Class Distribution
plt.subplot(3, 2, 1)
outcome_counts = df_cleaned['Outcome'].value_counts()
colors = ['#2ecc71', '#e74c3c']
plt.bar(outcome_counts.index, outcome_counts.values, color=colors, alpha=0.7, edgecolor='black')
plt.xlabel('Outcome', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Class Distribution: Diabetic vs Non-Diabetic', fontsize=14, fontweight='bold')
plt.xticks([0, 1], ['Non-Diabetic', 'Diabetic'])
for i, v in enumerate(outcome_counts.values):
    plt.text(i, v + 10, str(v), ha='center', fontweight='bold')

# Plot 2: Correlation Heatmap
plt.subplot(3, 2, 2)
correlation_matrix = df_cleaned.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', 
            linewidths=0.5, cbar_kws={'shrink': 0.8})
plt.title('Correlation Heatmap', fontsize=14, fontweight='bold')

# Plot 3: Glucose Distribution
plt.subplot(3, 2, 3)
plt.hist(df_cleaned['Glucose'], bins=30, color='#3498db', alpha=0.7, edgecolor='black')
plt.xlabel('Glucose Level', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Glucose Distribution', fontsize=14, fontweight='bold')
plt.axvline(df_cleaned['Glucose'].mean(), color='red', linestyle='--', 
            linewidth=2, label=f'Mean: {df_cleaned["Glucose"].mean():.1f}')
plt.legend()

# Plot 4: BMI Distribution
plt.subplot(3, 2, 4)
plt.hist(df_cleaned['BMI'], bins=30, color='#9b59b6', alpha=0.7, edgecolor='black')
plt.xlabel('BMI (Body Mass Index)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('BMI Distribution', fontsize=14, fontweight='bold')
plt.axvline(df_cleaned['BMI'].mean(), color='red', linestyle='--', 
            linewidth=2, label=f'Mean: {df_cleaned["BMI"].mean():.1f}')
plt.legend()

# Plot 5: Age Distribution
plt.subplot(3, 2, 5)
plt.hist(df_cleaned['Age'], bins=20, color='#e67e22', alpha=0.7, edgecolor='black')
plt.xlabel('Age (years)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Age Distribution', fontsize=14, fontweight='bold')
plt.axvline(df_cleaned['Age'].mean(), color='red', linestyle='--', 
            linewidth=2, label=f'Mean: {df_cleaned["Age"].mean():.1f}')
plt.legend()

# Plot 6: Diabetic vs Non-Diabetic Comparison
plt.subplot(3, 2, 6)
diabetic = df_cleaned[df_cleaned['Outcome'] == 1]['Glucose']
non_diabetic = df_cleaned[df_cleaned['Outcome'] == 0]['Glucose']
plt.hist([non_diabetic, diabetic], bins=20, color=['#2ecc71', '#e74c3c'], 
         label=['Non-Diabetic', 'Diabetic'], alpha=0.7, edgecolor='black')
plt.xlabel('Glucose Level', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Glucose: Diabetic vs Non-Diabetic', fontsize=14, fontweight='bold')
plt.legend()

plt.tight_layout()
plt.savefig('EDA_Visualizations.png', dpi=300, bbox_inches='tight')
print("✓ EDA visualizations saved as 'EDA_Visualizations.png'\n")
plt.show()

# =============================================================================
# PART 3: MODEL TRAINING AND EVALUATION
# =============================================================================
print("\n" + "="*80)
print(" PART 3: MODEL TRAINING AND EVALUATION ".center(80))
print("="*80 + "\n")

# Prepare data for training
print("Preparing data for model training...")
X = df_cleaned.drop('Outcome', axis=1)
y = df_cleaned['Outcome']

# Split the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                      random_state=42, stratify=y)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Training set size: {X_train.shape[0]} samples")
print(f"Test set size: {X_test.shape[0]} samples\n")

# Initialize models
print("Training multiple models...")
print("-" * 80)

models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100),
    'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5)
}

# Train and evaluate each model
results = {}

for model_name, model in models.items():
    print(f"\nTraining {model_name}...")
    
    # Train the model
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Store results
    results[model_name] = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1,
        'Model': model
    }
    
    print(f"✓ {model_name} trained successfully!")
    print(f"  Accuracy: {accuracy:.4f}")

# Create comparison table
print("\n" + "="*80)
print(" MODEL PERFORMANCE COMPARISON ".center(80))
print("="*80 + "\n")

results_df = pd.DataFrame(results).T
results_df = results_df.drop('Model', axis=1)
results_df = results_df.round(4)
print(results_df.to_string())
print()

# Select the best model based on accuracy
best_model_name = results_df['Accuracy'].idxmax()
best_model = results[best_model_name]['Model']
best_accuracy = results_df['Accuracy'].max()

print("="*80)
print(f"🏆 BEST MODEL: {best_model_name}")
print(f"🎯 ACCURACY: {best_accuracy:.4f} ({best_accuracy*100:.2f}%)")
print("="*80 + "\n")

# Save model comparison
results_df.to_csv('model_comparison.csv')
print("✓ Model comparison saved as 'model_comparison.csv'\n")

# Visualize model comparison
plt.figure(figsize=(12, 6))

metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
x = np.arange(len(results_df.index))
width = 0.2

for i, metric in enumerate(metrics):
    plt.bar(x + i*width, results_df[metric], width, label=metric, alpha=0.8)

plt.xlabel('Models', fontsize=12, fontweight='bold')
plt.ylabel('Score', fontsize=12, fontweight='bold')
plt.title('Model Performance Comparison', fontsize=14, fontweight='bold')
plt.xticks(x + width*1.5, results_df.index, rotation=15, ha='right')
plt.legend()
plt.ylim(0, 1.1)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('Model_Comparison.png', dpi=300, bbox_inches='tight')
print("✓ Model comparison chart saved as 'Model_Comparison.png'\n")
plt.show()

# =============================================================================
# PART 4: FEATURE IMPORTANCE ANALYSIS
# =============================================================================
print("\n" + "="*80)
print(" PART 4: FEATURE IMPORTANCE ANALYSIS ".center(80))
print("="*80 + "\n")

# Get feature importance (works for tree-based models)
if hasattr(best_model, 'feature_importances_'):
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': best_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print("Feature Importance Ranking:")
    print("-" * 80)
    for idx, row in feature_importance.iterrows():
        print(f"{row['Feature']:25s}: {row['Importance']:.4f}")
    
    print()
    
    # Visualize feature importance
    plt.figure(figsize=(10, 6))
    colors = plt.cm.viridis(feature_importance['Importance'] / feature_importance['Importance'].max())
    plt.barh(feature_importance['Feature'], feature_importance['Importance'], color=colors, edgecolor='black')
    plt.xlabel('Importance Score', fontsize=12, fontweight='bold')
    plt.ylabel('Health Indicators', fontsize=12, fontweight='bold')
    plt.title(f'Feature Importance - {best_model_name}', fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('Feature_Importance.png', dpi=300, bbox_inches='tight')
    print("✓ Feature importance chart saved as 'Feature_Importance.png'\n")
    plt.show()
    
    print("\n💡 INSIGHT: The most influential health indicators for diabetes prediction are:")
    for i, row in feature_importance.head(3).iterrows():
        print(f"   {i+1}. {row['Feature']} (Importance: {row['Importance']:.4f})")
    print()
else:
    print(f"⚠ Feature importance not available for {best_model_name}")
    print("   (Available only for tree-based models)\n")

# =============================================================================
# PART 5, 6 & 7: INTERACTIVE PREDICTION SYSTEM WITH RISK METER & REPORT
# =============================================================================

def print_risk_meter(probability):
    """Display visual risk meter"""
    risk_percentage = probability * 100
    
    # Determine risk category
    if risk_percentage < 30:
        risk_level = "LOW RISK"
        color_code = "🟢"
    elif risk_percentage < 70:
        risk_level = "MODERATE RISK"
        color_code = "🟡"
    else:
        risk_level = "HIGH RISK"
        color_code = "🔴"
    
    # Create visual bar (20 blocks total)
    filled_blocks = int(risk_percentage / 5)
    empty_blocks = 20 - filled_blocks
    visual_bar = "█" * filled_blocks + "░" * empty_blocks
    
    print("\n" + "="*80)
    print(" DIABETES RISK METER ".center(80))
    print("="*80)
    print(f"\n{visual_bar}  {color_code} {risk_level}")
    print(f"\nRisk Probability: {risk_percentage:.1f}%")
    print("="*80 + "\n")

def get_top_contributing_factors(patient_data, feature_names, top_n=3):
    """Identify top contributing factors for prediction"""
    if hasattr(best_model, 'feature_importances_'):
        importance = best_model.feature_importances_
        # Normalize patient data to see relative contribution
        contributions = []
        for i, feature in enumerate(feature_names):
            contributions.append((feature, importance[i], patient_data[i]))
        
        # Sort by importance
        contributions.sort(key=lambda x: x[1], reverse=True)
        return contributions[:top_n]
    else:
        # For non-tree models, return top features by value
        feature_values = list(zip(feature_names, patient_data))
        feature_values.sort(key=lambda x: abs(x[1]), reverse=True)
        return feature_values[:top_n]

def generate_patient_report(patient_data_dict, prediction, probability, top_factors):
    """Generate comprehensive patient report card"""
    
    risk_percentage = probability * 100
    
    # Determine risk category
    if risk_percentage < 30:
        risk_category = "LOW RISK"
        recommendation = "✓ Maintain healthy lifestyle with regular exercise and balanced diet."
    elif risk_percentage < 70:
        risk_category = "MODERATE RISK"
        recommendation = "⚠ Monitor health indicators regularly. Consider lifestyle modifications and consult healthcare provider."
    else:
        risk_category = "HIGH RISK"
        recommendation = "⚠ Consult a healthcare professional immediately for comprehensive evaluation and management."
    
    # Print report
    print("\n" + "="*80)
    print(" PATIENT DIABETES RISK REPORT ".center(80))
    print("="*80 + "\n")
    
    print("📋 PATIENT SUMMARY")
    print("-" * 80)
    for key, value in patient_data_dict.items():
        print(f"{key:30s}: {value}")
    
    print("\n" + "-" * 80)
    print("🎯 PREDICTION RESULTS")
    print("-" * 80)
    if prediction == 1:
        print(f"Prediction: DIABETIC ⚠")
    else:
        print(f"Prediction: NON-DIABETIC ✓")
    
    print(f"Risk Category: {risk_category}")
    print(f"Prediction Confidence: {risk_percentage:.1f}%")
    
    print("\n" + "-" * 80)
    print("📊 TOP CONTRIBUTING FACTORS")
    print("-" * 80)
    for i, factor in enumerate(top_factors[:3], 1):
        if len(factor) == 3:  # Tree-based model
            print(f"{i}. {factor[0]} (Importance: {factor[1]:.4f}, Value: {factor[2]:.2f})")
        else:  # Other models
            print(f"{i}. {factor[0]} (Value: {factor[1]:.2f})")
    
    print("\n" + "-" * 80)
    print("💊 RECOMMENDATIONS")
    print("-" * 80)
    print(f"{recommendation}")
    
    print("\n" + "="*80 + "\n")

def predict_diabetes_risk():
    """Interactive prediction system"""
    
    print("\n" + "="*80)
    print(" INTERACTIVE DIABETES RISK PREDICTION ".center(80))
    print("="*80 + "\n")
    
    print("Please enter patient health information:\n")
    
    try:
        # Collect user inputs
        pregnancies = float(input("Pregnancies (number of times pregnant): "))
        glucose = float(input("Glucose (mg/dL): "))
        blood_pressure = float(input("Blood Pressure (mm Hg): "))
        skin_thickness = float(input("Skin Thickness (mm): "))
        insulin = float(input("Insulin (mu U/ml): "))
        bmi = float(input("BMI (Body Mass Index): "))
        dpf = float(input("Diabetes Pedigree Function (0.0 - 2.5): "))
        age = float(input("Age (years): "))
        
        # Create patient data dictionary
        patient_data_dict = {
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'Blood Pressure': blood_pressure,
            'Skin Thickness': skin_thickness,
            'Insulin': insulin,
            'BMI': bmi,
            'Diabetes Pedigree Function': dpf,
            'Age': age
        }
        
        # Prepare data for prediction
        patient_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, 
                                  insulin, bmi, dpf, age]])
        
        # Scale the data
        patient_data_scaled = scaler.transform(patient_data)
        
        # Make prediction
        prediction = best_model.predict(patient_data_scaled)[0]
        probability = best_model.predict_proba(patient_data_scaled)[0][1]
        
        # Get top contributing factors
        top_factors = get_top_contributing_factors(patient_data[0], X.columns)
        
        # Display risk meter
        print_risk_meter(probability)
        
        # Generate full report
        generate_patient_report(patient_data_dict, prediction, probability, top_factors)
        
        return True
        
    except ValueError:
        print("\n❌ Error: Please enter valid numeric values!")
        return False
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        return False

# =============================================================================
# MAIN EXECUTION - INTERACTIVE PREDICTION
# =============================================================================

# Run the interactive prediction system
print("\n" + "="*80)
print(" READY FOR PREDICTION ".center(80))
print("="*80)

while True:
    print("\nOptions:")
    print("1. Make a new prediction")
    print("2. Exit")
    
    choice = input("\nEnter your choice (1 or 2): ")
    
    if choice == '1':
        predict_diabetes_risk()
    elif choice == '2':
        print("\n" + "="*80)
        print(" Thank you for using the Diabetes Risk Prediction System! ".center(80))
        print("="*80)
        break
    else:
        print("❌ Invalid choice! Please enter 1 or 2.")

print("\n✓ All results and visualizations saved successfully!")
print("\nGenerated Files:")
print("  - diabetes_cleaned.csv")
print("  - EDA_Visualizations.png")
print("  - Model_Comparison.png")
print("  - Feature_Importance.png")
print("  - model_comparison.csv")
print("\n" + "="*80)
print(" PROJECT COMPLETED SUCCESSFULLY! ".center(80))
print("="*80 + "\n")
