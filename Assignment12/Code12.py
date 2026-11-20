import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

df = pd.read_csv("customer_churn.csv")

print("First 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nColumn Names:")
print(df.columns)

numeric_columns = df.select_dtypes(include="number").columns

print("\nDescriptive Statistics:")

for col in numeric_columns:
    print("\nColumn:", col)
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Mode:", df[col].mode().iloc[0])
    print("Standard Deviation:", df[col].std())
    print("Variance:", df[col].var())
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())
    print("Quantiles:")
    print(df[col].quantile([0.25, 0.50, 0.75]))


# Histogram
if len(numeric_columns) > 0:
    col1 = numeric_columns[0]

    plt.hist(df[col1].dropna(), bins=10, edgecolor="black")
    plt.title("Histogram")
    plt.xlabel(col1)
    plt.ylabel("Frequency")
    plt.show()

    # Box Plot
    sns.boxplot(y=df[col1])
    plt.title("Box Plot")
    plt.show()

# Scatter Plot
if len(numeric_columns) >= 2:
    col1 = numeric_columns[0]
    col2 = numeric_columns[1]

    plt.scatter(df[col1], df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title("Scatter Plot")
    plt.show()

# Correlation Heatmap
if len(numeric_columns) > 0:
    correlation = df[numeric_columns].corr()

    sns.heatmap(correlation, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

# Step 6: Handle Missing Data
print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna().copy()

print("\nDataset After Removing Missing Values:")
print(df.head())

numeric_columns = df.select_dtypes(include="number").columns

z_scores = df[numeric_columns].apply(zscore)

outlier_mask = (z_scores.abs() > 3).any(axis=1)

print("\nDetected Outliers:")
print(df[outlier_mask])

df_cleaned = df.loc[~outlier_mask].copy()

print("\nDataset After Removing Outliers:")
print(df_cleaned)

print("\nRemaining Missing Values:")
print(df_cleaned.isnull().sum())

final_z_scores = df_cleaned[numeric_columns].apply(zscore)

remaining_outliers = (final_z_scores.abs() > 3).any(axis=1)

print("\nRemaining Outlier Rows:")
print(remaining_outliers.sum())

~df_cleaned.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")