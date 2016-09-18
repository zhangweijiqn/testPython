from pandas import Series, DataFrame
import pandas as pd
obj = Series([4, 7, -5, 3])
print obj.values
print obj.index

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print obj2['a']
print obj2[['c', 'a', 'd']]
obj2['d'] = 6
print obj2[obj2 > 0]
print 'b' in obj2


sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
print obj4  # only include the key in dictionary



