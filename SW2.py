###import os - ###don't need this unless changing path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as matplotlib
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

#extract pandas arrays of date and snow water equivalent
df_date = sw['DATE(UTC)']
df_sw_3a20p = sw['3A20P Callaghan']
df_sw_3a25p = sw['3A25P Squamish River Upper']
df_sw_1D06P = sw['1D06P Tenquille Lake']

#convert pandas into np arrays for use with plt
np_date = np.array(df_date)
np_sw_3a20p = np.array(df_sw_3a20p)
np_sw_3a25p = np.array(df_sw_3a25p)
np_sw_1D06P = np.array(df_sw_1D06P)

#plot date and swe
plt.scatter(np_date, np_sw_3a20p)
plt.scatter(np_date, np_sw_3a25p)
plt.scatter(np_date, np_sw_1D06P)

#add title
plt.title("Seasons Snow Water for Callghan, Squamish Valley, Tenquille Lake")

#add legend - not done yet
#plt.legend(["Snow Water Equivalent", "Snowfall"])

#play with axes - not done yet
#matplotlib.axes.Axes.secondary_yaxis("Snowfall")

#show plot
plt.show()