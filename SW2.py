###import os - ###don't need this unless changing path
import numpy as np
import pandas as pd
import matplotlib as matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

#delete old csv file
try:
    os.remove("SW.csv")
    print("Previous File Removed!")
except:
    print('File could not be removed')

#or download CSV if i can figure that out!!
### here is the link to the csv: http://www.env.gov.bc.ca/wsd/data_searches/snow/asws/data/SW.csv ###
import wget
url = 'http://www.env.gov.bc.ca/wsd/data_searches/snow/asws/data/SW.csv'
print('Beginning download of file using wget from',url)
wget.download(url, 'SW.csv')

#read csv
sw = pd.read_csv("SW.csv")

#initialize plt and setup params
plt.figure(figsize=(15, 8), dpi=100)

#plot date and swe
plt.plot(sw['DATE(UTC)'], sw['3A20P Callaghan'])
plt.plot(sw['DATE(UTC)'], sw['3A25P Squamish River Upper'])
plt.plot(sw['DATE(UTC)'], sw['1D06P Tenquille Lake'])

#add title
plt.title("Seasons Snow Water for Callghan, Squamish Valley, Tenquille Lake")

# todo - adding legend to the curve - Not Working
plt.legend()

# todo - fix x axis spacing of dates because they are all crammed together
plt.xlabel('Date')

#show plot
plt.show()