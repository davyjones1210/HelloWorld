#Create dataframes
import pandas as pd
import numpy as np
import openpyxl
dates=pd.date_range('today',periods=6) #define time sequence as index
print(dates)
num_arr = np.random.randn(6,4) #import numpy random array
print(num_arr)
columns = ['A','B,','C','D']    #use the table as the column name
df1=pd.DataFrame(num_arr, index = dates, columns=columns)
print(df1)

#Create dataframe with dictionary array
data = {'animal':['cat','cat','snake','dog','dog','cat','snake','cat','dog','dog'],
        'age':[2.5,3,0.5,np.nan,5,2,4.5,np.nan,7,3],
        'visits': [1,3,2,3,2,3,1,1,2,1],
        'priority':['yes','yes','no','yes','no','no','no','yes','no','no']}
labels = ['a','b','c','d','e','f','g','h','i','j']
df2=pd.DataFrame(data, index=labels)
print(df2)
print(df2.dtypes)
df3= df2.head(6)
print(df3)
df4= df2.tail(3)
print(df4)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())   #See statistics data of dataframes
print(df2.T)
print(df2.sort_values(by='age'))

#Slicing dataframe
print(df2[1:3])
print(df2[['age','visits']])
print(df2.iloc[1:3])    #Query rows 2,3
df3=df2.copy()
print(df3)
#df3.isnull()
print(df3.isnull())
df3.loc['f','age']=1.5
print(df3)
print(df3[['age']].mean())
print(df3[['visits']].mean())
print(df3[['visits']].sum())
print(df3.sum())

string = pd.Series(['A','C','D','Aaa','BaCa',np.nan,'CBA','cow','owl'])
print(string)
print(string.str.upper())

#Operations for data frame missing values
df4 = df3.copy()
# meanAge = df4['age'].mean()
# print(df4.fillna(4))
# print(df4['age'].fillna(meanAge))
df5 = df3.copy()
print(df5.dropna(how='any'))

#Dataframe file operations

#df3.to_csv('animal.csv')
#df_animal = pd.read_csv('animal.csv')
#print(df_animal.head(3))
#df3.to_excel('animal1.xlsx', sheet_name= 'Sheet1')
df3.to_excel('animal2.xlsx', sheet_name='Sheet1')
df_animal2 = pd.read_excel('animal2.xlsx','Sheet1', index_col=None, na_values = ['NA'])
print(df_animal2)

