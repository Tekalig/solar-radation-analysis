import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.data_processing import data_loader
from src.time_series_analysis import time_series_analysis
from src.bubble_chart import create_bubble_chart
from src.temperature_analysis import analyze_temperature_humidity
from src.histograms import plot_histograms
from src.z_score_analysis import calculate_z_scores, flag_outliers
from src.wind_analysis import plot_wind_analysis


def main(file_path, dataset_name):
    """
    Main function to perform EDA on the dataset.
    Parameters:
        file_path (str): The file path to the CSV file.
        dataset_name (str): The name of the dataset for titles.
    """

    #  Load data
    df = data_loader(file_path, parse_dates=["Timestamp"])

    # Time series analysis
    figures = time_series_analysis(df, dataset_name=dataset_name)
    # Save the figures in the screenshots folder
    for i, fig in enumerate(figures):
        fig.savefig(
            f"screenshots/{dataset_name.lower()}_time_series_analysis_{i}.png"
        )
        plt.close(fig)

    #  Bubble chart
    # Define variables for the bubble chart
    x_column = "GHI"
    y_column = "Tamb"
    bubble_size_column = "RH"  # Relative Humidity
    bubble_color_column = "BP"  # Barometric Pressure
    title = f"{dataset_name}: GHI vs. Tamb vs. RH (size) & BP (color)"
    fig = create_bubble_chart(
        df, x_column, y_column, bubble_size_column, bubble_color_column, title
    )
    fig.savefig("screenshots/togo_bubble_chart.png")
    plt.close(fig)

    # Temperature analysis
    fig = analyze_temperature_humidity(df, dataset_name)
    fig.savefig(f"screenshots/{dataset_name.lower()}_temperature_analysis.png")
    plt.close(fig)

    # Histograms Plot
    fig = plot_histograms(df, dataset_name)
    fig.savefig(f"screenshots/{dataset_name.lower()}_histogram.png")
    plt.close(fig)

    # Z-Score analysis
    # Specify columns for Z-score calculation
    columns_to_check = ["GHI", "DNI", "DHI", "ModA", "ModB", "WS", "WSgust"]
    # Perform Z-score analysis for Sierra Leone dataset
    z_scores, outliers = calculate_z_scores(df, columns_to_check)
    new_df = flag_outliers(df, z_scores, columns_to_check)
    # Display results
    print(
        f"{dataset_name} dataset outliers flagged:\n",
        new_df["Outlier_Flag"].value_counts(),
    )

    # Wind Rose data analysis
    fig = plot_wind_analysis(df, dataset_name)
    fig.savefig(f"screenshots/{dataset_name.lower()}_wind_analysis.png")
    plt.close(fig)


if __name__ == "__main__":
    # Example usage
    file_path = "data/processed/cleaned_togo.csv"
    dataset_name = "Togo"
    main(file_path, dataset_name)
