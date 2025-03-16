import pandas as pd
import numpy as np

def data_quality_check(df, columns):
    """
    Perform data quality checks on specified columns of a DataFrame.

    Parameters:
        df (pd.DataFrame): The DataFrame to check.
        columns (list): List of columns to check for data quality issues.

    Returns:
        dict: A dictionary with quality issues and summary statistics.
    """
    quality_issues = {}
    for col in columns:
        if col not in df.columns:
            continue
        # Check for missing values
        missing_values = df[col].isnull().sum()

        # Check for negative values
        negative_values = (df[col] < 0).sum()

        # Check for outliers using IQR
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()

        # Save the findings
        quality_issues[col] = {
            "Missing Values": missing_values,
            "Negative Values": negative_values,
            "Outliers": outliers,
        }

    return quality_issues


def summarize_quality_issues(issues):
    """
    Print a summary of the quality issues found.

    Parameters:
        issues (dict): The dictionary of quality issues.
    """
    print("Data Quality Check Summary:")
    for col, stats in issues.items():
        print(f"Column: {col}")
        for issue, count in stats.items():
            print(f"  {issue}: {count}")
        print("-" * 40)
