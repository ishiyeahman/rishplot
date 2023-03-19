import matplotlib.pyplot as plt
import rishplot

def plot_mosaic(layout, data, titles=None, xlabels=None, ylabels=None, legends=None):
    """
    Plot data on a grid of subplots using the subplot_mosaic function of matplotlib.

    Args:
        layout (list): List that specifies the layout of subplots.
        data (list): List of dictionaries, where each dictionary specifies the data and options for one subplot.
                     Each dictionary should have the following keys: 'type', 'x', and 'y'.
                     'type' specifies the type of plot to be created ('line', 'scatter', or 'bar').
                     'x' and 'y' are lists or arrays of data to be plotted on the x- and y-axes.
                     'type' can also be 'scatter' or 'bar' for scatter and bar plots, respectively.
                     If 'type' is 'scatter', the dictionary can also include the 'c' key, which specifies the color
                     for each point.
                     If 'type' is 'bar', the dictionary can also include the 'width' key, which specifies the width
                     of each bar.
        titles (list): List of subplot titles.
        xlabels (list): List of x-axis labels.
        ylabels (list): List of y-axis labels.
        legends (list): List of legends for each subplot.

    Returns:
        None
    """
    # Create a new figure object
    fig = plt.figure(constrained_layout=True)

    # Create a dictionary of Axes objects based on the given layout using subplot_mosaic function
    ax_dict = fig.subplot_mosaic(layout)

    # Plot data on the corresponding Axes object for each argument passed in
    for key, plot_data in zip(ax_dict.keys(), data):

        plot_type = plot_data['type']
        if plot_type == 'line':
            ax_dict[key].plot(plot_data['data'][0], plot_data['data'][1])
        elif plot_type == 'scatter':
            ax_dict[key].scatter(plot_data['data'][0], plot_data['data'][1], c=plot_data.get('c', None))
        elif plot_type == 'bar':
            ax_dict[key].bar(plot_data['data'][0], plot_data['data'][1], width=plot_data.get('width', 0.8))
        else:
            print(f"Invalid plot type for subplot {key}")

    # Set titles, xlabels, ylabels, and legends for each subplot
    if titles is not None:
        for key, title in zip(ax_dict.keys(), titles):
            ax_dict[key].set_title(title)
    if xlabels is not None:
        for key, xlabel in zip(ax_dict.keys(), xlabels):
            ax_dict[key].set_xlabel(xlabel)
    if ylabels is not None:
        for key, ylabel in zip(ax_dict.keys(), ylabels):
            ax_dict[key].set_ylabel(ylabel)
    if legends is not None:
        for key, legend in zip(ax_dict.keys(), legends):
            if legend:
                ax_dict[key].legend(legend)

    # Display the created figure object
    plt.show()