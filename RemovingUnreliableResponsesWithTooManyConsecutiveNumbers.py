#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# If a response has more than 12 of the same number in a row, delete response with that id from dataframe
# (ex. deleting response where answer strongly agree more than 12 times in a row since this response 
# most likely isn't reliable)


# Print response id where answer strongly disagree 12 or more times
for n in range(len(data)):
    df2 = data.iloc[n]
    numZero = 0
    for i in range(len(ques)):
        Q = ques[i]
        if (df2[Q] == 0):
            numZero += 1
        if (numZero == 12):
            print(df2.ID)
            
            
# Print response id where answer strongly agree 12 or more times
for n in range(len(data)):
    df1 = data.iloc[n]
    numSix = 0
    for i in range(len(ques)):
        Q = ques[i]
        if (df1[Q] == 6):
            numSix += 1
        if (numSix == 12):
            print(df2.ID)
            
            
# Do the same for responses with 12 or more of the same consectutive answers for dissagree through agree
check = [1,2,3,4]

for x in check:
    for n in range(len(data)):
        df2 = data.iloc[n]
        numConsecutive = 0
        for i in range(len(ques)):
            Q = ques[i]
            if (df2[Q] == x):
                numConsecutive += 1
            if (numConsecutive == 12):
                print(df2.ID)
                


for ind in delete_these_indexes_consecutive_nums:
    data.drop([ind], inplace=True)

