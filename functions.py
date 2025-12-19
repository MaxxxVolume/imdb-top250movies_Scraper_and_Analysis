import matplotlib.pyplot as plt


def show_grid(style="--", width=0.8, alpha=0.3, color="#cccccc"):
    """
    This simple function just displays a grid in the next plot.
    The parameters are predefined for faster usage.

    Args:
        style (str): Determines the linestyle, predefined as --
        width (float): Determines the linewidth, predefined as 0.8
        alpha (float): Determines the alpha of the lines, predefined as 0.3
        color (str): Determines the color of the gridlines, predefined as #cccccc (for dark background)

    Returns:
        None
    """
    plt.grid(True, linestyle=style, linewidth=width, alpha=alpha, color=color)
