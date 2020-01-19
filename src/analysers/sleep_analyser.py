from src.utilities.utilities import read_from_file
from src.plot.plot_sleep import plot_sleep_cycles
import regex as re

def analyse_sleep_data():
    masterText = read_from_file('Sleep/Master.txt')

    basicInfoCheck = re.compile(r"(\"awakeningsCount\").*?([0-9]+).*?(\"duration\").*?([0-9]+).*?(\"efficiency\").*?([0-9]+).*?(\"endTime\").*?([0-9]+-[0-9]+-[0-9]+[A-z]{1})([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]+).*?(\"isMainSleep\").*?([A-z]{4,5})",re.MULTILINE)
    basicInfo = basicInfoCheck.findall(masterText)

    cycleInfoCheck = re.compile(r"(\"timeInBed\").*?([0-9]+).*?(\"deep\").*?([0-9]+).*?(\"light\").*?([0-9]+).*?(\"rem\").*?([0-9]+).*?(\"wake\").*?([0-9]+).*?(\"totalMinutesAsleep\").*?([0-9]+)",re.MULTILINE)
    cycleInfo = cycleInfoCheck.findall(masterText)

    startInfoCheck = re.compile(r"(\"startTime\").*?([0-9]+-[0-9]+-[0-9]+[A-z]{1})([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]+).*?(\"totalSleepRecords\").*?([0-9]{1})",re.MULTILINE)
    startInfo = startInfoCheck.findall(masterText)

    ## IDK, figure this shit out
    realbasicInfo = list()
    for basic in basicInfo:
        if basic[10] == 'true':
            realbasicInfo.append(basic)

    realstartInfo = list()
    for start in startInfo:
        if start[4] == '1':
            realstartInfo.append(basic)

    # plotSST(realbasicInfo,realstartInfo)

    ## FUTURE TO-DO???
    # sleepInfoCheck = re.compile(r"(\"dateTime\").*?([0-9]{2}:[0-9]{2}:[0-9]{2}).*?(\"value\").*?([1-3])",re.MULTILINE)
    # sleepInfo = sleepInfoCheck.findall(masterText)

    # plotPAA(cycleInfo)
    plot_sleep_cycles(cycleInfo)

    print(0)