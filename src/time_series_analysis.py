import matplotlib.pyplot as plt
import seaborn as sns


def time_series_analysis(data, dataset_name):
    """
    Perform time series analysis on a dataset.

    Parameters:
        data (pd.DataFrame): The dataset to analyze.
        dataset_name (str): The name of the dataset for titles.
    """
    # Set Timestamp as the index
    data.set_index('Timestamp', inplace=True)

    # Plot GHI, DNI, DHI, and Tamb over time
    plt.figure(figsize=(14, 7))
    for col in ['GHI', 'DNI', 'DHI', 'Tamb']:
        data[col].plot(label=col)

    plt.title(f'Time Series of GHI, DNI, DHI, and Tamb - {dataset_name}')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Monthly aggregation for trends
    monthly_data = data.resample('ME').mean()
    plt.figure(figsize=(14, 7))
    for col in ['GHI', 'DNI', 'DHI']:
        monthly_data[col].plot(label=col)

    plt.title(f'Monthly Average of Solar Radiation Components - {dataset_name}')
    plt.xlabel('Month')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Evaluate the impact of cleaning on sensor readings
    cleaned_data = data[data['Cleaning'] == 1]
    uncleaned_data = data[data['Cleaning'] == 0]

    plt.figure(figsize=(14, 7))
    sns.lineplot(x=cleaned_data.index, y=cleaned_data['ModA'], label=f'ModA (Cleaned) - {dataset_name}', color='blue')
    sns.lineplot(x=uncleaned_data.index, y=uncleaned_data['ModA'], label=f'ModA (Uncleaned) - {dataset_name}',
                 color='orange')
    sns.lineplot(x=cleaned_data.index, y=cleaned_data['ModB'], label=f'ModB (Cleaned) - {dataset_name}', color='green')
    sns.lineplot(x=uncleaned_data.index, y=uncleaned_data['ModB'], label=f'ModB (Uncleaned) - {dataset_name}',
                 color='red')

    plt.title(f'Impact of Cleaning on Sensor Readings (ModA and ModB) - {dataset_name}')
    plt.xlabel('Time')
    plt.ylabel('Sensor Values')
    plt.legend()
    plt.grid(True)
    plt.show()
