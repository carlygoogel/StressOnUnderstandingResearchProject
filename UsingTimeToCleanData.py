#!/usr/bin/env python
# coding: utf-8

# # Cleaning Data By Removing Responses That Took Less Than Five Minutes To Complete

# Import data
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
data = pd.read_csv('Stress and Understanding Survey Final.csv')


# Use timestamps if time spent is less than 5 minutes ==> delete response
# Change string start and end dates into double datatypes and append into startTime and endTime lists
deletedIndexes = [3, 18, 80, 96, 109, 212, 359, 77, 124, 173, 204, 233, 235, 274, 293, 330, 345] # Deleted due to too many null

startTime = []
endTime = []

for i in range(len(data)):
    # Account for indexes already deleted based on null values
    if i in deletedIndexes:
        continue
    else:
        str1 = data['Start Date'][i]
        x = str1[14:19]
        x = x.replace(':', '.', 2)
        x = float(x)
        startTime.append(x)
    
for i in range(len(data)):
    if i in deletedIndexes:
        continue
    else:
        str2 = data['End Date'][i]
        x = str2[14:19]
        x = x.replace(':', '.', 2)
        x = float(x)
        endTime.append(x)
        
print(f'Start Time: {startTime[:5]}')
print(f'End Time: {endTime[:5]}')


# Create list of times based on difference in end time and start time

times = []

for i in range(len(startTime)):
    s = startTime[i]
    e = endTime[i]
    time = e - s
    times.append(time)

# Note: getting negative time means participant spent over an hour on the survey, need 
# to look these responses over to make sure reliable / decide to keep or rid
print(f'Times: {times[:5]}')



# Map times to response index in dictionary while accounting for the indexes that were previously deleted

timeDict = {}
timeOn = 0

for i in range(len(data)):
    if i in deletedIndexes:
        timeDict[i] = 'deleted'
    else:
        timeDict[i] = times[timeOn]
        timeOn += 1

from itertools import islice
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

five_items = take(5, timeDict.items())
print(five_items)



# Print response index with time spent for where time is less than 5 minutes

for i in range(len(timeDict)):
    if timeDict[i] == 'deleted':
        continue
    else:
        x = timeDict[i]
        x = abs(x)
        x = round(x, 3)
        if x < 5:
            print(f'Index: {i}')
            print(f'Time: {x}')
            print('\n')

