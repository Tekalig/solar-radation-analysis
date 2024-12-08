import pandas as pd
import numpy as np

def handle_missing_values(df):
    """
    Handle missing values in the dataset by imputing or dropping.
    Parameters:
        df (pd.DataFrame): The input DataFrame.
    Returns:
        pd.DataFrame: The DataFrame with missing values handled.
    """
    # Impute missing values with the median for numeric columns
    df.fillna(df.median(numeric_only=True), inplace=True)
    return df


def handle_negative_values(df, columns):
    """
    Replace negative values with NaN and then impute using median.
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list): List of columns to check for negative values.
    Returns:
        pd.DataFrame: The DataFrame with negative values handled.
    """
    for col in columns:
        df[col] = df[col].apply(lambda x: np.nan if x < 0 else x)
    df.fillna(df.median(numeric_only=True), inplace=True)
    return df


def handle_outliers(df, columns, threshold=3):
    """
    Handle outliers in the dataset using the Z-score method.
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list): List of columns to check for outliers.
        threshold (float): The Z-score threshold to identify outliers.
    Returns:
        pd.DataFrame: The DataFrame with outliers handled.
    """
    for col in columns:
        col_mean = df[col].mean()
        col_std = df[col].std()
        z_scores = (df[col] - col_mean) / col_std
        # Cap outliers to the upper and lower threshold values
        df[col] = np.where(z_scores.abs() > threshold, col_mean, df[col])
    return df


def clean_data(df):
    """
    Perform full data cleaning: missing values, negative values, and outliers.
    Parameters:
        df (pd.DataFrame): The input DataFrame.
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # List of columns to check for negatives and outliers
    numeric_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']

    df = handle_missing_values(df)
    df = handle_negative_values(df, numeric_columns)
    df = handle_outliers(df, numeric_columns)
    return df