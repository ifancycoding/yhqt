# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:26:56 2018

@author: wuwangchuxin
"""
import os
os.chdir('D:/yh_min-mfactors')
from address_data import *
import feather as ft
import pandas as pd
import pickle

daily = ft.read_dataframe(add_day_file + 'marketData.feather')

daily_2016 = daily[daily['date']>='2016-01-01']
daily_2016 = daily_2016[['date','symbol','close','preClose']]

daily_2016['daily_return'] = (daily_2016['close']-daily_2016['preClose'])*100/daily_2016['preClose']

output=open(add_gene_file + 'dailyreturn.pickle','wb')
pickle.dump(daily_2016,output) 
output.close()