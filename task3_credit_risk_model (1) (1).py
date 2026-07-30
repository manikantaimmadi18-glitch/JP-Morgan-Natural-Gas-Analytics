import pandas as pd

# Load the dataset
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

import pandas as pd

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Features (X)
X = df.drop(columns=["customer_id", "default"])

# Target (y)
y = df["default"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Model accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Predict Probability of Default (PD)
probabilities = model.predict_proba(X_test)

# Probability of default is the second column
pd_values = probabilities[:, 1]

# Create a results DataFrame
results = X_test.copy()
results["Actual_Default"] = y_test.values
results["Predicted_PD"] = pd_values

# Recovery Rate = 10%
recovery_rate = 0.10
loss_given_default = 1 - recovery_rate

# Expected Loss
results["Expected_Loss"] = (
    results["Predicted_PD"]
    * results["loan_amt_outstanding"]
    * loss_given_default
)

print("\nTop 10 Predictions:")
print(results[["loan_amt_outstanding", "Predicted_PD", "Expected_Loss"]].head(10))

results.to_csv("credit_risk_predictions.csv", index=False)

print("\nResults saved as credit_risk_predictions.csv")

""""
Project Overview – Credit Risk Prediction Model

Objective:
Developed a Credit Risk Prediction Model to estimate the Probability of Default (PD) for borrowers and calculate the Expected Loss (EL) using borrower financial information.

Tools Used:

Python
Pandas
Scikit-learn
Logistic Regression
VS Code

Methodology:

Loaded and explored the loan dataset.
Performed data preprocessing and checked for missing values.
Selected relevant borrower features and split the data into training and testing sets.
Trained a Logistic Regression model to predict loan defaults.
Evaluated the model using Accuracy, Confusion Matrix, and Classification Report.
Predicted the Probability of Default (PD) and calculated Expected Loss (EL) for each borrower.
Exported the final predictions to a CSV file for further analysis.

Outcome:
The model achieved 99.7% accuracy and successfully estimated borrower default probabilities and expected losses, providing a reliable prototype for credit risk assessment and lending decisions.
    """