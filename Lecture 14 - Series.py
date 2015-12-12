import numpy as np
import pandas as pd

from pandas import Series, DataFrame


obj = Series([3,6,9,12])

print obj.index



ww2_cas = Series([8700000,4300000, 3000000, 2100000, 400000], index = ['USSR', 'Germany', 'China', 'Japan', 'USA'])

print ww2_cas


print ww2_cas['USA']


#Check which countries had casulaties greater than 4million

print ww2_cas[ww2_cas > 4000000]


print 'USSR' in ww2_cas

ww2_dict = ww2_cas.to_dict()

print ww2_dict

ww2_series = Series(ww2_dict)

print ww2_series


countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']

obj2 = Series(ww2_dict, index= countries)

print obj2

print ww2_series + obj2

obj2.name = "World War 2 casualties"

print obj2

obj2.index.name = 'Countries'

print obj2
