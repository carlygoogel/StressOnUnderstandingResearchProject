#!/usr/bin/env python
# coding: utf-8

# Removing responses with null values


# Checking For nulls Values On PSS questions 
df1 = data[['ID','PSSQ1','PSSQ2','PSSQ3','PSSQ4','PSSQ5','PSSQ6','PSSQ7','PSSQ8','PSSQ9','PSSQ10']]
df1 = df1[df1.isna().any(axis=1)]
print(df1)


delete_indexes_null_pss = [3, 18, 80, 96, 109, 212, 359]

for ind in delete_indexes_null_pss:
    data.drop([ind], inplace=True)


# Using the entire dateframe, remove responses that have more than 4 null values (accounting for
# optional answer to 2 logic open ended question and accidental question skips)

ques = df.columns
IDNull = []

for i in range(len(df1)):
    df2 = df.iloc[i]
    numNaN = 0
    for x in range(len(ques)):
        Q = ques[x]
        if ((df2[Q] is not int) | (df2[Q] is not float)):
            numNaN += 1
        if (numNaN == 4):
            print(df2.ID)
            IDNull.append(df2.ID)
            

delete_indexes_too_many_null = [77, 124, 173, 204, 233, 235, 274, 293, 330, 345, 357]

for ind in delete_indexes_too_many_null:
    data.drop([ind], inplace=True)

