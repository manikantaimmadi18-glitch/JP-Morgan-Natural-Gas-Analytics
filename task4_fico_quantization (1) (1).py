import pandas as pd
import numpy as np


df = pd.read_csv("Task 3 and 4_Loan_Data.csv")


print("First 5 Rows:")
print(df.head())


print("\nDataset Information:")
print(df.info())


print("\nMissing Values:")
print(df.isnull().sum())


print("\nFICO Score Summary:")
print(df["fico_score"].describe())



num_buckets = 5


df["Rating"] = pd.qcut(
    df["fico_score"],
    q=num_buckets,
    labels=[5, 4, 3, 2, 1]
)


_, boundaries = pd.qcut(
    df["fico_score"],
    q=num_buckets,
    retbins=True
)

print("\nBucket Boundaries:")
print(boundaries)

print("\nSample Rating Map:")
print(df[["fico_score", "Rating"]].head(20))


df.to_csv("fico_rating_map.csv", index=False)

print("\nRating map saved as fico_rating_map.csv")

"""""
Task 4: FICO Score Quantization

Objective:
Convert continuous FICO scores into discrete credit rating categories.

Method:
- Load the loan dataset.
- Analyse the FICO score distribution.
- Create 5 equal-frequency rating buckets using pd.qcut().
- Assign ratings from 1 (best) to 5 (highest risk).
- Save the final rating map as fico_rating_map.csv.

Tools Used:
- Python
- Pandas
- NumPy
"""