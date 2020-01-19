## PLOT PERCENTAGE OF TIME IN BED SPENT ASLEEP VS AWAKE
import datetime
import statistics
import matplotlib.pyplot as plt

def plotPAA(cycleInfo):
    first_date = datetime.date(2018,1,1)
    last_date = datetime.date(2018,12,31)

    times = list()
    delta = last_date - first_date
    for i in range(delta.days + 1):
        timeInBed = float(cycleInfo[i][1])
        timeAsleep = float(cycleInfo[i][11])
        awakeSleepPercentage = (timeAsleep/timeInBed)*100
        if awakeSleepPercentage < 100:
            times.append(((first_date + datetime.timedelta(i)).strftime("%Y-%b-%d"), awakeSleepPercentage))

    # duration is in miliseconds
    # what is efficiency?

    x_val = [time[0] for time in times]
    y_val = [time[1] for time in times]
    y_med = statistics.mean(y_val)

    backgroundColor = "#022a31"
    medColor = "#66cccc"
    lineColor = "#088da5"
    markerColor = "#ff4040"
    figColor = "#014351"
    textColor = "#66cccc"


    plt.axhline(y=y_med, color=medColor, linestyle='--')
    plt.plot(x_val,y_val,lineColor)
    plt.plot(x_val,y_val,marker="o",color=markerColor,linestyle = 'None')
    plt.title('Percentage of Time in Bed Spent Sleeping', fontsize=18, color=textColor)

    ax = plt.gca()
    fig = plt.gcf()

    plt.xticks(fontsize=14, rotation=45,color=textColor)
    plt.yticks(fontsize=14,color=textColor)
    
    fig.canvas.set_window_title('Percentage of Time Asleep vs Awake')


    n = 30  # Keeps every 10th label
    [l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]

    ax.set_facecolor(backgroundColor)
    fig.patch.set_facecolor(figColor)

    props = dict(boxstyle='round', facecolor=medColor, alpha=0.5)

    medString = '\n'.join((
        ("Highest: "+str(round(max(y_val),2))+"%"),
        ("Lowest: "+str(round(min(y_val),2))+"%"),
        ("Median: "+str(round(y_med,2))+"%")))

    # place a text box in upper left in axes coords
    ax.text(0.05, 0.95,medString, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)

    plt.show()