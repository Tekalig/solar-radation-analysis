import matplotlib.pyplot as plt

def plot_histograms(data, dataset_name):
    """
    Plots histograms for key variables to visualize their frequency distribution.

    Parameters:
        data (pd.DataFrame): The dataset containing the variables.
        dataset_name (str): Name of the dataset (e.g., "Togo", "Benin").
    """
    columns_to_plot = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'TModA', 'TModB']
    num_columns = len(columns_to_plot)
    num_rows = (num_columns + 2) // 3  # To arrange plots in 3 columns

    fig, axes = plt.subplots(num_rows, 3, figsize=(15, 5 * num_rows))
    axes = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        if col in data.columns:
            axes[i].hist(data[col].dropna(), bins=20, color='skyblue', edgecolor='black', alpha=0.7)
            axes[i].set_title(f"Histogram of {col} ({dataset_name})")
            axes[i].set_xlabel(col)
            axes[i].set_ylabel("Frequency")
        else:
            axes[i].set_title(f"{col} not found in {dataset_name}")
            axes[i].axis('off')  # Hide axes if the column doesn't exist

    # Hide any extra subplots
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()

    print(f"Histograms plotted for {dataset_name}.")
