import pandas as pd

data =pd.read_csv('NBA-playerlist.csv')
#returns a list of columns 
print(data.columns)
print('******************')
#returns the (numrows,numcols)
print(data.head())
#returns type of each column
types = data.dtypes

print(types)
'''Preparing data for analysis by cleaning it.
The code below does the following:
- drops columns, and duplicates
- fixes missing values
- checks for null values
'''
data.columns
newData=data[['DISPLAY_LAST_COMMA_FIRST',
       'FROM_YEAR', 'GAMES_PLAYED_FLAG',
       'PERSON_ID', 'PLAYERCODE', 'ROSTERSTATUS', 'TEAM_ABBREVIATION',
       'TEAM_CITY', 'TEAM_CODE', 'TEAM_ID', 'TEAM_NAME', 'TO_YEAR']]

#to fix missing values I filled it with a non impactful value of unknown
data['TEAM_ID'] = data['TEAM_ID'].fillna('unknown')

#check for null values
print('NULL VALUES CHECK')
print(data.isnull().sum())

data.drop_duplicates(inplace=True)
#bins=
#pd.cut(data['col'],bins=bins,labels=labels, include_lowest=True,right=False)


'''
Doing a sanity check to make sure the data reflects the problem we are trying to solve
'''
data['GAMES_PLAYED_FLAG'].value_counts()