import matplotlib.pyplot as plt
from windrose import WindroseAxes


def plot_wind_analysis(data, dataset_name):
    """
    Generates wind rose plots to analyze wind speed and direction distribution.

    Parameters:
        data (pd.DataFrame): The dataset containing wind speed and direction.
        dataset_name (str): The name of the dataset (e.g., "Togo", "Benin").
    """
    if "WS" not in data.columns or "WD" not in data.columns:
        print(f"Dataset {dataset_name} does not contain required wind columns.")
        return

    ws = data["WS"].dropna()
    wd = data["WD"].dropna()

    fig = plt.figure(figsize=(8, 8))
    ax = WindroseAxes.from_ax(fig=fig)
    ax.bar(wd, ws, normed=True, opening=0.8, edgecolor="white")
    ax.set_title(f"Wind Rose for {dataset_name}")
    ax.set_legend(title="Wind Speed (m/s)")
    plt.tight_layout()
    return fig