import matplotlib.pyplot as plt


def create_bubble_chart(data, x_col, y_col, bubble_size_col, bubble_color_col, title):
    """
    Create a bubble chart to visualize the relationship between variables.

    Parameters:
        data (pd.DataFrame): Dataset containing the variables.
        x_col (str): Column name for the x-axis variable.
        y_col (str): Column name for the y-axis variable.
        bubble_size_col (str): Column name for bubble size.
        bubble_color_col (str): Column name for bubble color.
        title (str): Title of the chart.

    Returns:
        plt.Figure: The created bubble chart figure.
    """
    plt.figure(figsize=(12, 8))
    fig, ax = plt.subplots()
    scatter = ax.scatter(
        data[x_col],
        data[y_col],
        s=data[bubble_size_col] * 10,  # Adjust size scaling as needed
        c=data[bubble_color_col],
        cmap="viridis",
        alpha=0.7,
        edgecolors="w",
        linewidth=0.5,
    )
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    plt.colorbar(scatter, ax=ax, label=bubble_color_col)
    return fig
