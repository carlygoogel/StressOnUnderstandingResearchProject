#!/usr/bin/env python
# coding: utf-8

# Getting ready to analyze data now that it's clean

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
data = pd.read_csv('Stress and Understanding Survey Final.csv')
data.head()


# Calculate PSS Score Following Guidelines For Tool

def mapPSSPos(x):
    if x == 'never':
        return 0
    elif x == 'almost never':
        return 1
    elif x == 'sometimes':
        return 2
    elif x == 'fairly often':
        return 3
    elif x == 'very often':
        return 4
    
def mapPSSNeg(x):
    if x == 'never':
        return 4
    elif x == 'almost never':
        return 3
    elif x == 'sometimes':
        return 2
    elif x == 'fairly often':
        return 1
    elif x == 'very often':
        return 0
    
data['PSSQ1'] = data.PSSQ1.apply(mapPSSPos)
data['PSSQ2'] = data.PSSQ2.apply(mapPSSPos)
data['PSSQ3'] = data.PSSQ3.apply(mapPSSPos)
data['PSSQ4'] = data.PSSQ4.apply(mapPSSNeg)
data['PSSQ5'] = data.PSSQ5.apply(mapPSSNeg)
data['PSSQ6'] = data.PSSQ6.apply(mapPSSPos)
data['PSSQ7'] = data.PSSQ7.apply(mapPSSNeg)
data['PSSQ8'] = data.PSSQ8.apply(mapPSSNeg)
data['PSSQ9'] = data.PSSQ9.apply(mapPSSPos)
data['PSSQ10'] = data.PSSQ10.apply(mapPSSPos)


# Summing values across PSS questions
PSSList = ['PSSQ1','PSSQ2','PSSQ3','PSSQ4','PSSQ5','PSSQ6','PSSQ7','PSSQ8','PSSQ9','PSSQ10']
data['PSSScore'] = data[PSSList].sum(axis=1)
data[['PSSQ1','PSSQ2','PSSQ3','PSSQ4','PSSQ5','PSSQ6','PSSQ7','PSSQ8','PSSQ9','PSSQ10', 'PSSScore']].head(10)


# Graphing PSS Scores in Boxplot

import matplotlib.pyplot as plt
plt.boxplot(data.PSSScore)
plt.title('PSS Score')
plt.show()


# Graphing PSS Scores in Histogram

import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

x = data.PSSScore

plt.hist(x, density=True, bins=40)  # density=False would make counts
plt.ylabel('Amount')
plt.xlabel('Score')
plt.show()



# Using two values less than the lower quartile and three values more than the third quartile to determine
# low, moderate, and high stress groups in order to ensure all groups have a suffient amount of responses

def mapPSSNumberSignificance(x):
    if x <= 18:
        return 'low stress'
    elif x < 24:
        return 'moderate stress'
    else:
        return 'high stress'

# Add a new column to dataframe for PSS Stress Level (low, moderate, or high)
data['PSS_Stress_Level'] = data.PSSScore.apply(mapPSSNumberSignificance)




# Mapping all likert scale to ordinal values for the rest of the questions

col_to_map = ["PandemicQ1", "PandemicQ2", "PandemicQ3"]

for col in col_to_map:
    data[col] = data[col].map({"Strongly disagree": 0, "Disagree": 1, "Somewhat disagree": 2, "Neither agree or disagree": 3, "Somewhat agree": 4, "Agree": 5, "Strongly agree":6})
    
print(data['PandemicQ1'].value_counts())

pandemicStressList = ["PandemicQ1", "PandemicQ2", "PandemicQ3"]
data['PandemicStressNum'] = data[pandemicStressList].sum(axis=1)

# Generating basic graphs as go
plt.clf()
plt.boxplot(data.PandemicStressNum)
plt.title('Pandemic Stress Score')
plt.show()

plt.clf()
plt.scatter(data.PSSScore, data.PandemicStressNum)
plt.xlabel('PSS Score')
plt.ylabel('Pandemic Stress Score')
plt.title('PSS Score vs Pandemic Stress Level')
plt.show()


cols_to_map = ['aware_different_feelings_I_felt', 'not_aware_those_feelings',
       'aware_my_thoughts', 'experiencing_present_fully', 'felt_aware_alert',
       'noticed_small_details_in_experience',
       'able_logically_think_through_strong_negative_emotions',
       'know_strongest_qualitites', 'know_what_brings_me_joy',
       'can_think_strategies_use_stay_calm_stressful_situations',
       'can_think_environments_where_would_be_in_positive_mindset',
       'I am confused about why the friend has this emotion',
       'The emotion of the friend was caused by his or her own behavior',
       'The emotion of the friend was caused by your actions',
       'The emotion of the friend was caused by circumstances out of anyone’s control',
       'I would take action to further understand or resolve the friend’s emotion',
       'I thought more about the situation from how it could affect my relationship with the friend as opposed to the emotion of the friend',
       'I am very confused why the friend has this emotion (1)',
       'The emotion of the friend was caused by his or her own behavior (1)',
       'The emotion of the friend was caused by your actions (1)',
       'The emotion of the friend was caused by circumstances out of anyone’s control (1)',
       'I would take action to further understand or resolve the friend’s emotion (1)',
       'I thought more about the situation from how it could affect my relationship with the friend as opposed to the emotion of the friend (1)',
       'I feel like I have a strong understanding of that person’s emotions',
       'I know what that person is thinking',
       'I feel strong emotions for that person  (feel bad for them, happy for them, etc)',
       'I wish I could help the person in this situation',
       'I feel like I have a strong understanding of that person’s emotions (1)',
       'I know what that person is thinking (1)',
       'I feel strong emotions for that person  (feel bad for them, happy for them, etc) (1)',
       'I wish I could help the person in this situation (1)',
       'I feel like I have a strong understanding of that person’s emotions (2)',
       'I know what that person is thinking (2)',
       'I feel strong emotions for that person (feel bad for them, happy for them, etc) (2)',
       'I feel like I have a strong understanding of that person’s emotions (3)',
       'I know what that person is thinking (3)',
       'I feel strong emotions for that person (feel bad for them, happy for them, etc) (3)',
       'I would like the friend to pay more attention to what I’m saying',
       'I am annoyed with the friend',
       'I considered that the friend might have an external reason to check the time (running late, etc)',
       'I should pay more attention to what the friend is saying',
       'I am annoyed with myself',
       'I considered that I might have an external reason to check the time (running late, etc)',
       'I am justified in asking the person to pay for the meal',
       'I am annoyed with the person',
       'I considered the emotional effect the situation would have on me',
       'I considered the emotional effect the situation might have had on the other person',
       'The person is justified in asking me to pay for the meal',
       'I am annoyed with myself.1',
       'I considered the emotional effect the situation would have on me.1',
       'I considered the emotional effect the situation might have had on the other person.1']

for col in cols_to_map:
    data[col] = data[col].map({"Strongly disagree": 0, "Disagree": 1, "Somewhat disagree": 2, "Neither agree or disagree": 3, "Somewhat agree": 4, "Agree": 5, "Strongly agree":6})
    
print(data['aware_my_thoughts'].value_counts())




# Grouping data by stress level and storing new grouped dataframe to be able to upload to new filw
df = df.groupby(['PSS_Stress_Level']).agg(list)
df.head()
get_ipython().run_line_magic('store', 'df')

high = df.iloc[0]
low = df.iloc[1]
med = df.iloc[2]




# Printing mean values by stress level for each question

def means_across_questions_values(ques):
    question = ques
    hm = np.nanmean(high[question])
    lm = np.nanmean(low[question])
    mm = np.nanmean(med[question])

    print(f'{question}\n{hm}\n{lm}\n{mm} \n \n')
    

for i in range(len(df.columns)):
    means_across_questions_values(df.columns[i])




# Function to print three way by stress level box chart for any question
# Input question or list of question

import seaborn as sns
import matplotlib.pyplot as plt

def boxChartHLM(question, Qnum):
    h = df.iloc[0,Qnum]
    l = df.iloc[1,Qnum]
    m = df.iloc[2,Qnum]

    print(question)
    plt.figure(figsize=(8,2))
    ax1 = plt.subplot(2,2,1)
    sns.boxplot(x=h)
    plt.title('high stress')
    plt.xlim([0,6])
    plt.show()

    plt.figure(figsize=(8,2))
    ax2 = plt.subplot(2,2,2)
    sns.boxplot(x=m)
    plt.title('moderate stress')
    plt.xlim([0,6])
    plt.show()

    plt.figure(figsize=(8,2))
    ax3 = plt.subplot(2,2,3)
    sns.boxplot(x=l)
    plt.title('low stress')
    plt.xlim([0,6])
    plt.show()
    plt.clf()
    
    
z = df.columns[6:11]

for i in range(len(z)):
    quest = z[i]
    num = df.columns.get_loc(quest)
    boxChartHLM(quest, num)




# For fun: Printing circle charts of responses to all questions

# See how majority people answered each question
import matplotlib.pyplot as plt

def collapse_category(feat, threshold):
    '''Needed to ensure that only a mask would be used to mark categories to collapse,
    and to preserve the original data frame'''
    sum = data1[feat].value_counts(dropna = False).reset_index()[feat].sum()
    temp = data1[feat].copy()
    mask1 = temp.value_counts()/sum < threshold
    mask2 = temp.isin(mask1[mask1 == True].index)
    temp[mask2] = 'other'
    return temp.value_counts(dropna = False).reset_index()


for i in range(1, 12):
    plt.figure(figsize = (16, 9))
    j = 2*i
    k = j-2
    for num, feat in zip(range(1,3), for_plotting[k:j]):
        plt.subplot(1, 2, num)
        temp = collapse_category(feat, 0.01)
        labels = temp['index']
        theme = plt.get_cmap("tab20" if len(labels) > 10 else "tab10")
        plt.pie(x=temp[feat], autopct="%.1f%%", labels=labels, pctdistance=0.77,
                #radius = 1,
                colors = theme(np.arange(len(labels))),
                wedgeprops=dict(width=0.10,
                                edgecolor="k",
                                linewidth=0.7))
        text = feat
        plt.text(0, 0, text, 
                 horizontalalignment = 'center',
                 verticalalignment = 'center',
                 fontsize = 20)
    plt.show()
    plt.clf()

