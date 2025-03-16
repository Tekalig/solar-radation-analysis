import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def analyze_temperature_humidity(data, dataset_name):
    """
    Examines how relative humidity (RH) influences temperature and solar radiation.

    Parameters:
        data (pd.DataFrame): The dataset containing RH, temperature, and solar radiation data.
        dataset_name (str): The name of the dataset (e.g., "Togo", "Benin").
    """
    if 'RH' not in data.columns:
        print(f"Dataset {dataset_name} does not contain 'RH' column.")
        return

    columns_to_plot = ['Tamb', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']
    fig, axes = plt.subplots(len(columns_to_plot), 1, figsize=(10, 20), sharex=True)

    for i, col in enumerate(columns_to_plot):
        sns.scatterplot(x=data['RH'], y=data[col], ax=axes[i], alpha=0.6)
        axes[i].set_title(f"RH vs {col} ({dataset_name})")
        axes[i].set_xlabel("Relative Humidity (%)")
        axes[i].set_ylabel(col)

    plt.tight_layout()
    plt.show()

    print(f"Temperature analysis completed for {dataset_name}.")
