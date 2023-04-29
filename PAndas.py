import pandas as pd
import matplotlib.pyplot as plt
#print(pd.__version__)
a=[10,11,12]
"""""myvar=pd.Series(a)
print(myvar[0])"""
"""""myvar=pd.Series(a,index=['a','s','d'])
print(myvar)
print(myvar['a'])"""
s={'calories':[1,2,3],'bug':[4,5,6]}
""""myvar=pd.DataFrame(s)
print(myvar)
print(myvar.loc[1])"""
myvar=pd.read_csv('data.csv')
"""""print(myvar.to_string())#will print all of it
print(pd.options.display.max_rows)
pd.options.display.max_rows=999999
print(myvar)"""
#print(myvar.info())
df=pd.read_csv('dirtydata.csv')
#df1=df.dropna()#remove the Nan inplcae to change the original file
##print(df1.to_string())
#print(df.to_string())
#df.fillna(130,inplace=True)
#print(df.to_string())
#df['Date']=pd.to_datetime(df['Date'])
#print(df.to_string())
""""df.dropna(subset=['Date'], inplace = True)
print(df.to_string())
df.loc[7, 'Duration'] = 45
df.drop(x)"""#to drop something not all
''''print(df.duplicated())
df.drop_duplicates(inplace=True)'''
df1=pd.read_csv('data (1).csv')
#print(df.corr())
df1.plot()
plt.show()