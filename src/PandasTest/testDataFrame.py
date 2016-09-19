#coding=utf8

#http://pda.readthedocs.io/en/latest/chp5.html

from pandas import Series, DataFrame
import pandas as pd
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print frame

frame2 = DataFrame(data, columns=['year', 'state', 'pop'])  #如果你传递了一个行，但不包括在 data 中，在结果中它会表示为NA值
print frame2

print frame2['state']

print frame2.year


