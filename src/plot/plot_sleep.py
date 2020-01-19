import datetime
import statistics
import matplotlib.pyplot as plt

backgroundColor = "#022a31"
meanColor = "#66cccc"
lineColor = "#088da5"
markerColor = "#ff4040"
figColor = "#014351"
textColor = "#66cccc"
DEEPColor = "#088da5"
LIGHTColor = "#66cccc"
REMColor = "#e1ad01" 
AWAKEColor = "#ff4040"
   
def plot_sleep_cycles(cycleInfo):
    
    # TODO: Maybe add another textbox containing the averages for each one...

    first_date = datetime.date(2018,1,1)
    last_date = datetime.date(2018,12,31)

    times = list()
    delta = last_date - first_date

    for i in range(delta.days + 1):
        timeDEEP = float(cycleInfo[i][3])
        timeLIGHT = float(cycleInfo[i][5])
        timeREM = float(cycleInfo[i][7])
        timeAWAKE = float(cycleInfo[i][9])

        if timeDEEP == 0:
            times.append(((first_date + datetime.timedelta(i)).strftime("%Y-%b-%d"), None,None,None,None))
        else:
            times.append(((first_date + datetime.timedelta(i)).strftime("%Y-%b-%d"), timeDEEP,timeLIGHT,timeREM,timeAWAKE))

    # duration is in miliseconds
    # what is efficiency?

    x_val = [time[0] for time in times]
    DEEP_val = [time[1] for time in times]
    LIGHT_val = [time[2] for time in times]
    REM_val = [time[3] for time in times]
    AWAKE_val = [time[4] for time in times]
    
    plt.plot(x_val,DEEP_val,DEEPColor)
    plt.plot(x_val,LIGHT_val,LIGHTColor)
    plt.plot(x_val,REM_val,REMColor)
    plt.plot(x_val,AWAKE_val,AWAKEColor)

    plt.title('Minutes Spent in Each Sleep Stage', fontsize=18, color=textColor)

    ax = plt.gca()
    fig = plt.gcf()

    plt.xticks(fontsize=14, rotation=45,color=textColor)
    plt.yticks(fontsize=14,color=textColor)
    
    fig.canvas.set_window_title('Minutes Spent in Each Sleep Stage')


    n = 30  # Keeps every 10th label
    [l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]

    ax.legend(['Deep', 'Light', 'REM','Awake'])

    ax.set_facecolor(backgroundColor)
    fig.patch.set_facecolor(figColor)

    # medString = '\n'.join((
    #     ("Highest: "+str(round(max(y_val),2))+"%"),
    #     ("Lowest: "+str(round(min(y_val),2))+"%"),
    #     ("Median: "+str(round(y_med,2))+"%")))
    ## place a text box in upper left in axes coords
    # ax.text(0.05, 0.95,medString, transform=ax.transAxes, fontsize=14,
    #         verticalalignment='top', bbox=props)

    plt.show()

def plot_time_spent_in_bed(cycleInfo):
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
    y_mean = statistics.mean(y_val)

    plt.axhline(y=y_mean, color=meanColor, linestyle='--')
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

    props = dict(boxstyle='round', facecolor=meanColor, alpha=0.5)
    dataString = '\n'.join((
        ("Highest: "+str(round(max(y_val),2))+"%"),
        ("Lowest: "+str(round(min(y_val),2))+"%"),
        ("Mean: "+str(round(y_mean,2))+"%")))
    # place a text box in upper left in axes coords
    ax.text(0.05, 0.95, dataString, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)
    plt.show()

def plot_sleep_start_stop(realbasicInfo, realstartInfo):
    pass

def plot_awakenings(realbasicInfo):

    ax = plt.gca()
    fig = plt.gcf()
    ax.set_facecolor(backgroundColor)
    fig.patch.set_facecolor(figColor)

    awakening_data = []
    for real_basic_info in realbasicInfo:
        awakening_data.append(int(real_basic_info[1]))

    plt.plot(awakening_data, marker="o",color=markerColor,linestyle = 'None')
    mean_awakenings = statistics.mean(awakening_data)
    plt.axhline(y=mean_awakenings, color=meanColor, linestyle='--')

    fig.canvas.set_window_title('Awakenings during the night')
    plt.title('Awakenings during the night', fontsize=18, color=textColor)

    props = dict(boxstyle='round', facecolor=meanColor, alpha=0.5)
    dataString = '\n'.join((
        ("Highest: "+str(max(awakening_data))),
        ("Lowest: "+str(min(awakening_data))),
        ("Mean: "+str(round(mean_awakenings, 0)))))
    # place a text box in upper left in axes coords
    ax.text(0.05, 0.95, dataString, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)

    # ax.legend(['Awakenings', 'Average'])
    plt.xticks(fontsize=14, color=textColor)
    plt.yticks(fontsize=14, color=textColor)

    plt.show()
