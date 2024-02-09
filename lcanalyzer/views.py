"""Module containing code for plotting a lightcurve."""

from matplotlib import pyplot as plt
import pandas as pd
    
def plotUnfolded(data,mag_col,time_col,color='b',marker='.'):
    """
    Display plots of unfolded lightcurves in different bands.
    :param data: a table of observations of a single object in a single band
    :param mag_col: the name of the column with magnitudes to plot
    :param time_col: the name of the column with time stamps
    :param color: the color of the plotted data points; default is: 'b'
    :param marker: the marker of the plotted data points; default is: '.' 
    """
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(1,1,1)
    ax.scatter(
        data[time_col],
        data[mag_col],
        color=color,
        marker=marker
    )
    ax.minorticks_on()
    ax.set_xlabel("MJD (days)")
    ax.set_ylabel('Mag')
    ax.set_title('Light curve')
    fig.tight_layout()
    plt.show()

