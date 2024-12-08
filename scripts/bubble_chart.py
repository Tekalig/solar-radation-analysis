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
        None: Displays the bubble chart.
    """
    plt.figure(figsize=(12, 8))
    sizes = data[bubble_size_col] * 10  # Scale bubble size for better visualization
    scatter = plt.scatter(
        data[x_col],
        data[y_col],
        s=sizes,
        c=data[bubble_color_col],
        cmap='viridis',
        alpha=0.7,
        edgecolors="w"
    )
    plt.colorbar(scatter, label=bubble_color_col)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, alpha=0.3)
    plt.show()
