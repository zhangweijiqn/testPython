__author__ = 'zhangwj'
# coding=utf8
from IPython.core.pylabtools import figsize
import pandas as pd

pd.set_option('display.mpl_style', 'default')  # Make the graphs a bit prettier
figsize(15, 5)

# data with title in csv file
# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('../resources/train_titanic.csv',header=0)

# fixed_df = pd.read_csv('../resources/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
print df.shape
print df.dtypes

print df.info() #可以查看有没有空值

print df.describe() #统计每一列的count,mean,std,min,max,1/4,2/4,3/4

# Look at the first 1 rows
print df[:1]

print df.columns

#Age列
print df['Name']

#Age列类型，Series
print type(df['Age'])

#Age列的前10行
print df['Name'][0:10]
print df.Age[0:10]
#Age列的mean
print df['Age'].mean()

#选取多个列
print df[['Sex','Pclass','Age']]

# 过滤缺失值
df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]

#过滤
df[df['Age']>60]
df[df['Age']>60][['Sex','Pclass','Age','Survived']]



#数据清洗,增加一列
df['Gender'] = df['Sex'].map( lambda x: x[0].upper() )
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)



