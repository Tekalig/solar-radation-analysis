def calculate_z_scores(data, columns):
    """
    Calculate Z-scores for the specified columns in the dataset to identify outliers.

    Parameters:
        data (pd.DataFrame): The dataset containing the variables.
        columns (list): List of column names to calculate Z-scores for.

    Returns:
        pd.DataFrame: A DataFrame containing Z-scores for the specified columns.
        pd.DataFrame: A DataFrame indicating flagged outliers (True for outliers, False otherwise).
    """
    z_scores = data[columns].apply(lambda x: (x - x.mean()) / x.std())
    outliers = z_scores.abs() > 3  # Flag data points with Z-score > 3 as outliers
    return z_scores, outliers


def flag_outliers(data, z_scores, columns):
    """
    Add a column to the dataset indicating whether any of the specified columns have outliers.

    Parameters:
        data (pd.DataFrame): Original dataset.
        z_scores (pd.DataFrame): Z-scores DataFrame.
        columns (list): List of columns checked for outliers.

    Returns:
        pd.DataFrame: The updated dataset with a new "Outlier_Flag" column.
    """
    data["Outlier_Flag"] = z_scores[columns].abs().max(axis=1) > 3
    return data
