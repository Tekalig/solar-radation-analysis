import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def correlation_analysis(data, dataset_name, save_path=None):
    """
    Perform correlation analysis and generate plots for a dataset.

    Parameters:
        data (pd.DataFrame): The dataset to analyze.
        dataset_name (str): Name of the dataset for labeling plots.
        save_path (str, optional): Path to save the plots. Defaults to None.

    Returns:
        pd.DataFrame: Correlation matrix for the analyzed dataset.
    """
    # Select relevant columns for analysis
    columns_of_interest = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
    data_subset = data[columns_of_interest]

    # Compute the correlation matrix
    correlation_matrix = data_subset.corr()

    # Heatmap of Correlation Matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(f'Correlation Matrix for {dataset_name}')
    if save_path:
        plt.savefig(f"{save_path}/correlation_matrix_{dataset_name}.png")
    plt.show()

    # Pair Plot
    sns.pairplot(data_subset, diag_kind="kde", corner=True)
    plt.suptitle(f'Pair Plot for {dataset_name}', y=1.02)
    if save_path:
        plt.savefig(f"{save_path}/pair_plot_{dataset_name}.png")
    plt.show()

    return correlation_matrix
