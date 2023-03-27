#import pandas and matplotlib library
import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns
import numpy as np


## read csv file 
df = pd.read_csv('Adult/adult.csv')



## show all columns 
print(df.columns)


##display fisrt 10 rows
# print(df.head(10))


## Display last 10 rows
# print(df.tail(10))


## Find  shape of datafarme
# print(df.shape)
# (48842, 15)(row,columns)


## datas informations 
# print(df.info())


## get random 50% data sample 
# print(df.sample(frac=0.50))


## Check null value 
# print(df.isnull()) # get True and flase answer 
# print(df.isnull().sum()) # Get number or null values of all columns 


##Data cleaning 
# print(df.isin(['?']).sum()) #get totoal numbers 
# df['workclass']=df['workclass'].replace('?',np.nan) #replace it
# df['occupation']=df['occupation'].replace('?',np.nan) #replace it
# df['native-country']=df['native-country'].replace('?',np.nan) #replace it
# print(df.isin(['?']).sum()) #get totoal numbers 


## Find null value and drop it(not working ) 
# x = df.isnull().sum()*100/len(df)
# df.dropna(how='any',inplace=True)
# print(df.shape)


## Check dublicate data 
# dub = df.duplicated().any()
# print(dub) #oytput is ( True means ke duplicate data se)
# x = df.drop_duplicates()
# print(x.shape)


## Overall Statistic 
# print(df.describe())
# print(df.describe(include='all'))


## Drop columns  
# df.drop(['educational-num','capital-gain','capital-loss'],axis=1)
# print(df.columns)


## single column data info 
# print(df['age'].describe())
# df['age'].hist() # get graph
# plt.show()# get graph


## find total number of person age beetween 17 to 18
# print(sum((df['age']>=17)  & (df['age'] <=48)))
# # or
# print(sum(df['age'].between(17,48)))


## how many persone having bachelors and master degree
# x1= df['education']=='Bachelors'
# x2= df['education']=='Masters'
# print(len(df[x1|x2]))

## get values of salary 
# print(df['income'].unique()) # output : ['<=50K' '>50K']
# print(df['income'].value_counts()) 
#Output :
# <=50K    37155
# >50K     11687 

## replace data  salary 
# df.replace(to_replace=['<=50K' '>50K'],value=[0,1],inplace=True)
# print(df.head())


## Who get more salary male or female(Not working)
# print(df.groupby('sex')['income'].mean().sort_values(ascending=False))











































