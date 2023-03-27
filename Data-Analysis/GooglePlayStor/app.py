#import pandas and matplotlib library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


## read csv file 
df = pd.read_csv('GooglePlayStor/googleplaystore.csv')

# print(df.columns)
# (['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
#        'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
#        'Android Ver'],
#       dtype='object')


## find some spacific name In app name:
# print(df[df['App'].str.contains('Camera',case=False)])


## avrage rating 
# print(df['Rating'].mean)

## Unique 
# print(df['Category'].nunique())


##find Which categorty is highest rating 
# print(df.groupby('Category')['Rating'].mean().sort_values(ascending=False))


## Find % Star Apps 
# print(df[df['Rating']==5.0])
# print(df[df['Rating']==5.0]['Rating'])


## Highest rating app 
# print(df[df['Reviews'].max()==df['Reviews']])


#top 5 apps 
# index = df['Reviews'].sort_values(ascending=False).head().index
# print(df.iloc[index]['App'])


##convert string to int and find most downloded app-----------IMP TOPIC 

# print(df['Installs']) 
# df['Installs_1'] = df['Installs'].str.replace(',','')
# df['Installs_1'] = df['Installs_1'].str.replace('+','')
# df['Installs_1'] = df['Installs_1'].str.replace('Free','0')
# df['Installs_1']= df['Installs_1'].astype('int')
# print(df['Installs_1'].dtype)
# index = df['Installs_1'].sort_values(ascending=False).index
# print(df.iloc[index].head())




























