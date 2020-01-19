import matplotlib.pyplot as plt
import numpy as np
import statistics

backgroundColor = "#022a31"
DataColor = "#088da5"
figColor = "#014351"
textColor = "#66cccc"
markerColor = "#ff4040"
meanColor = "#66cccc"

def plot_average_BMP(x, y, timeList):

    plt.figure(1)
    y = list(y) 
    y.pop() # Remove erroneous 0 end-term
    plt.plot(y,marker="o", color=markerColor, linestyle='None')
    plt.title("Average daily BPM", fontsize=18, color=textColor)

    plt.xticks(fontsize=14, color=textColor)
    plt.yticks(fontsize=14, color=textColor)
    
    fig = plt.gcf()
    fig.canvas.set_window_title('Average daily BPM')

    locs, labels = plt.xticks() # Get locations and labels
    # plt.xticks(np.arange(0,len(timeList)),timeList, rotation=90)  # Set locations and labels

    ax = plt.gca()
    ax.set_xlabel('Time (seconds)', fontsize=18)
    ax.set_ylabel('BPM', fontsize=18)

    awake_heartreate = y[26000:80000]
    awake_mean = statistics.mean(awake_heartreate)
    plt.axhline(y=awake_mean, color=meanColor, linestyle='--')

    asleep_heartreate = y[0:26000] + y[80000:]
    asleep_mean = statistics.mean(asleep_heartreate)
    plt.axhline(y=asleep_mean, color=meanColor, linestyle='--')

    ax.set_facecolor(backgroundColor)
    fig.patch.set_facecolor(figColor)
    plt.grid()
    plt.show()
