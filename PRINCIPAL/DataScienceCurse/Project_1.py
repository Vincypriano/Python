import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

train_data = pd.read_excel('Data_Train.xlsx')

#print(train_data.head())
print(train_data.shape)
train_data.dropna(inplace=True)
print(train_data.isna().sum())
print(train_data.dtypes)

def change_into_datetime(col):
    train_data[col] = pd.to_datetime(train_data[col])


print(train_data.columns)
for i in ['Date_of_Journey', 'Dep_Time', 'Arrival_Time']:
    change_into_datetime(i)
    
print(train_data.dtypes)
train_data['journey_day'] = train_data['Date_of_Journey'].dt.day
train_data['journey_month'] = train_data['Date_of_Journey'].dt.month
print(train_data.head())

