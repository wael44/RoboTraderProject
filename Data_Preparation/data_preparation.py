import sys
sys.path.append('C:/Users/Wael/Desktop/RoboTraderProject')

import pandas as pd

from db.get import *
from db.insert import *
from Data_Preparation.technical_indicators import *


"""
Save TA to database for each instruments
"""

#get intruments names from database (dictionarie containing instrument name indexed by its symbol (EXEMPLE : {'AC': 'Accor SA', 'ACA': 'Crédit Agricole S.A.'}) )
intruments_names=get_intruments_names()

for instr_name in intruments_names.keys():
    #get data (data will be received at the form of list of dictionaries)
    ohlcv_data=get_ohlcv(str(instr_name))

    #Convert the list of dictionaries to Dataframe
    ohlcv_dataframe=pd.DataFrame(ohlcv_data)

    #Extract technical indicators of different timestamps
    technical_indicators_df = Set_multiple_timeframe_indicators(ohlcv_dataframe,10,30)
    
    #Saving TA to database
    insert_ta(str(instr_name), technical_indicators_df)


