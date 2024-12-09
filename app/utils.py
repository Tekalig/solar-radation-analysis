import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def clean_data(data):
    """
    Cleans the raw data by handling missing values, handling outliers, and ensuring data is ready for analysis.
    Args:
        data (pd.DataFrame): Raw data to clean.
    Returns:
        pd.DataFrame: Cleaned data ready for analysis.
    """
    # Handle missing values by dropping rows with essential columns missing data
    data.dropna(subset=['GHI', 'DNI', 'DHI'], inplace=True)

    # Handle unrealistic or negative entries, as solar radiation shouldn't be negative
    data['GHI'] = data['GHI'].apply(lambda x: x if x >= 0 else 0)
    data['DNI'] = data['DNI'].apply(lambda x: x if x >= 0 else 0)
    data['DHI'] = data['DHI'].apply(lambda x: x if x >= 0 else 0)

    # Optionally normalize sensor values if needed, additional data cleaning logic could go here
    data['ModA'] = data['ModA'].apply(lambda x: x if x >= 0 else 0)
    data['ModB'] = data['ModB'].apply(lambda x: x if x >= 0 else 0)

    # Return cleaned dataset
    return data


def time_series_analysis(data, variable):
    """
    Generates a time series plot for selected solar variables over time.
    Args:
        data (pd.DataFrame): Data to visualize.
        variable (str): The column/variable selected for plotting.
    Returns:
        matplotlib.figure.Figure: Matplotlib figure object with plotted results.
    """
    fig, ax = plt.subplots()
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])  # Ensure time is parsed properly
    ax.plot(data['Timestamp'], data[variable], label=variable)
    ax.set_title(f"Trends of {variable} over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel(variable)
    ax.legend()
    return fig


def correlation_analysis(data, variables):
    """
    Computes and visualizes correlations among selected variables.
    Args:
        data (pd.DataFrame): Dataset to compute correlations on.
        variables (list): List of variable names for analysis.
    Returns:
        DataFrame: Correlation matrix
    """
    corr_matrix = data[variables].corr()  # Calculate correlation matrix
    return corr_matrix


def plot_histograms(data, variable, ax):
    """
    Plots histograms with KDE for a selected environmental/sensor variable.
    Args:
        data (pd.DataFrame): The dataset to plot.
        variable (str): The variable to create the histogram for.
        ax (matplotlib.axes.Axes): The matplotlib axis to draw on.
    """
    sns.histplot(data[variable].dropna(), kde=True, ax=ax)
    ax.set_title(f"Histogram for {variable}")
    ax.set_xlabel(variable)


def detect_outliers(data, variable, method="zscore", threshold=3):
    """
    Detects outliers in data using statistical methods like Z-Score or IQR.
    Args:
        data (pd.DataFrame): Dataset to analyze.
        variable (str): Variable to check for outliers.
        method (str): Method of outlier detection ('zscore' or 'iqr').
        threshold (float): Threshold value for outlier detection.
    Returns:
        pd.DataFrame: DataFrame with an outlier flag for the selected variable.
    """
    if method == "zscore":
        # Calculate z-score and identify points above threshold
        mean = data[variable].mean()
        std = data[variable].std()
        data['Outlier'] = ((data[variable] - mean) / std).abs() > threshold
    elif method == "iqr":
        # Interquartile range method for outlier detection
        Q1 = data[variable].quantile(0.25)
        Q3 = data[variable].quantile(0.75)
        IQR = Q3 - Q1
        data['Outlier'] = ((data[variable] < (Q1 - 1.5 * IQR)) | (data[variable] > (Q3 + 1.5 * IQR)))
    else:
        raise ValueError("Invalid method specified. Use 'zscore' or 'iqr'.")

    return data


def wind_analysis(data):
    """
    Analyzes wind speed and direction trends over time and returns distributions in visualization.
    Args:
        data (pd.DataFrame): Dataset containing wind speed and direction data
    Returns:
        matplotlib.figure.Figure: A visualization object to plot wind speed trends
    """
    fig, ax = plt.subplots()
    sns.histplot(
        data['WSgust'].dropna(),
        kde=True,
        ax=ax,
        label="Wind Gusts"
    )
    ax.set_title("Wind Gusts Distribution")
    ax.set_xlabel('Wind Speed')
    return fig
