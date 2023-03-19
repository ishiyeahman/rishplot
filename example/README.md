# rishplot - example

## 1. multiple figure

run [sample_mosaic.py](example/src/sample_mosaic.py)
### Usage

The `plot_mosaic` function can be used to create a grid of subplots with different types of plots on each subplot. The function takes in the following arguments:

* `layout` (list): List that specifies the layout of subplots.
* `data` (list): List of dictionaries, where each dictionary specifies the data and options for one subplot. Each dictionary should have the following keys: `type`, `data`, where `type` specifies the type of plot to be created (`line`, `scatter`, or `bar`). `data` is a list or array of data to be plotted on the x- and y-axes. `type` can also be `scatter` or `bar` for scatter and bar plots, respectively. If `type` is `scatter`, the dictionary can also include the `c` key, which specifies the color for each point. If `type` is `bar`, the dictionary can also include the `width` key, which specifies the width of each bar.
* `titles` (list): List of subplot titles.
* `xlabels` (list): List of x-axis labels.
* `ylabels` (list): List of y-axis labels.
* `legends` (list): List of legends for each subplot.

