import talib
import pandas as pd 
import numpy as np


import sys
sys.path.append('C:/Users/Wael/Desktop/RoboTraderProject')

from config import config
from Simulator.simulator import Simulator
from db.get import *
from db.insert import *



def calculate_slope(instr,period,save_to_db=False):
        """
        Calculate slopes of an instrument and save the to Database if save_to_db is set to true
        :param instr: Name of the instrument
        :param period: period to make the linear regression
        :param save_to_db: 
        :return: dataframe that contains slopes and indexed by date
        """

        ohlcv_data=get_ohlcv(instr,transform_to_dataframe=True) #ohlcv_data is dataframe containing open, high, low, close , adjusted prices , volume and date
        slopes=talib.LINEARREG_SLOPE(ohlcv_data[config.USED_CLOSE_PRICE], timeperiod=period)
        slopes_df=pd.DataFrame()
        slopes_df["Slope"]=slopes
        slopes_df.set_index(ohlcv_data["Date"],inplace=True)
        if save_to_db :
                slopes_df_db=slopes_df
                slopes_df_db["Date"]=slopes_df_db.index #date should be in column to save it in database
                insert_slopes(instr,slopes_df)

        return slopes_df


def best_thresh(instr,save_to_db=False):
        """
           :param instr:
           :param save_to_db: 
        """
        slopes=get_slopes(instr,transform_to_dataframe=True) #importing slopes and droping nan values
        slopes.dropna(inplace=True)
        slope_max=slopes["Slope"].describe().loc["max"]
        slope_min=slopes["Slope"].describe().loc["min"]
        threshs_up=np.linspace(0,slope_max,config.NUMBER_TRESHS)
        threshs_down=np.linspace(slope_min,0,config.NUMBER_TRESHS)
        #Grid Search
        threshs_list=[]
        for thresh_up in threshs_up:
                for thresh_down in threshs_down:
                        print("thresh_up: "+str(thresh_up)+"thresh_down: "+str(thresh_down))
                        decisions = [1 if slope>=thresh_up else -1 if slope<=thresh_down else 0 for slope in slopes["Slope"]]
                        solde=Simulator().simulate(instr,np.array(decisions),start=slopes["Date"].iloc[0])
                        thresh_dict={
                                "intrument":instr,
                                "thresh_up":thresh_up,
                                "thresh_down":thresh_down,
                                "solde":solde
                        }
                        threshs_list.append(thresh_dict)

        best_thresh=max(threshs_list,key=lambda item:item["solde"])
        if save_to_db:
                insert_best_thresh(instr,best_thresh)

        return best_thresh


        

    