#
#


import os
from time import striptime 
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# path and files...
load = pd.read_csv("Python Programming/HEN1_ET1_24-hr_10-03_07-35-12.txt")
Path_data=os.getcwd()
File_List=os.listdir(Path_data)

for ii, file in enumerate(File_List):
    print(file)

file='HEN1_ET1_24-hr_10-03_07-35-12.txt'

# read file
data=pd.read_table , sep='')
data # view data, note lack of column names 

#add column names 
data.columns = [ 'time', 'rr']
data

# plot the data... !!
plt.plot(data) 
plt.xlabel('time')
plt.ylabel('rr')
plt.show()

plt.plot(data.time, data.rr)
plt.show()

# convert <time> to minutes ... (your turn)


#create a datetime object with a specific time 
time='0.0' #second format
time_obj=strptime (time,'%S')
data['time__min']= data.time #change this...

#extract the time in minutes 
time_in_minutes=time_obj.minutes/60
print(time_in_minutes)
#convert <rr> to seconds...(your turn)
data['rr__s']= data.rr 

# you have now created two new columns 
data 

#plot two panels 
fig, ax=plt.subplots (2,1, figsize=(5,7)) 
# first plot 
ax[0].plot(data.time, data.rr) #original data 
ax[0].set_title('original data from file')
ax[0].set_xlabel('seconds')
ax[0].set_ylabel('seconds')
#second plot
ax[1].plot(data.time__min, data.rr__s) # new
vars
ax[1].set_title('converted units...')
ax[1].set_xlabel('should be minutes')
ax[1].set_ylabel('should be ms')
plt.tight_layout()
plt.show 

#end