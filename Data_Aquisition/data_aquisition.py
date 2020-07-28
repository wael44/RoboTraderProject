import pandas as pd
import numpy as np
import os
import sys
sys.path.append('C:/Users/Wael/Desktop/RoboTraderProject')

from db.insert import *
from config import config



"""
Import datasets (ohlcv prices for different instruments) from csv files and insert them to database
Save instruments Names to database
"""



data={}
for file_name in os.listdir(config.DATASET_PATH):
    #
    print(file_name.replace(".csv",""))
    data[file_name.replace(".csv","")]=pd.read_csv(os.path.join(config.DATASET_PATH,file_name))
    data[file_name.replace(".csv","")]['Date']=pd.to_datetime(data[file_name.replace(".csv","")]['Date'])
    
#data is dictionarie that contains ohlcv prices dataframe for every instrument. it's indexed by the intrument symbol
for symbol in data.keys():
    insert_ohlcv(str(symbol),data[str(symbol)])
    insert_instruments_names(str(symbol))