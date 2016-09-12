__author__ = 'zhangwj'
# coding=utf8
from IPython.core.pylabtools import figsize
import pandas as pd

pd.set_option('display.mpl_style', 'default')  # Make the graphs a bit prettier
figsize(15, 5)

# data with title in csv file
broken_df = pd.read_csv('../resources/train_titanic.csv')

# fixed_df = pd.read_csv('../resources/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
print broken_df.shape

# Look at the first 3 rows
print broken_df[:3]


print broken_df['Name']