import pandas as pd
import numpy as np


import sys
sys.path.append('C:/Wael/Usama/Desktop/RoboTraderProject')


from db.get import *
from config import config



"""
Simulator :
Profit calculation 
"""




class Simulator:
    def __init__(self):
        self.ohlcv_data=None
        self.instr=None



    def simulate_classifier(self,classifier):
        pass



    def get_tax(self,price,tax_rate):
        return price*tax_rate/100


    def simulate(self,instr,X,start=None,end=None,log=False,return_roi=False):
        self.ohlcv_data= get_ohlcv(instr ,start=start,end=end, transform_to_dataframe=True)
        self.ohlcv_data.set_index("Date",inplace=True)

        solde=config.INITIAL_SOLDE
        is_bought=False
        number_stocks=0

        for i in range(X.shape[0]):
            decision=round(X[i])
            if(decision==0):
                pass
            elif(decision==1 and not is_bought):
                number_stocks=int(solde/(self.ohlcv_data[config.BUY_PRICE].iloc[i] +self.get_tax(self.ohlcv_data[config.BUY_PRICE].iloc[i],config.TAX)))
                solde-=number_stocks*(self.ohlcv_data[config.BUY_PRICE].iloc[i] + self.get_tax(self.ohlcv_data[config.BUY_PRICE].iloc[i],config.TAX) )
                is_bought=True
                if log :
                    transaction={ 
                        "Date":self.ohlcv_data.index[i],
                        "Instrument Symbol": instr,
                        "Transaction Type":"buy",
                        "Number of stocks": number_stocks,
                        "Buy Price":self.ohlcv_data[config.BUY_PRICE].iloc[i],
                        "solde":solde

                    }
                    print(transaction)
            elif(decision==-1 and is_bought):
                solde+=(number_stocks*self.ohlcv_data[config.SELL_PRICE].iloc[i]) - self.get_tax(number_stocks* self.ohlcv_data[config.SELL_PRICE].iloc[i],config.TAX)
                is_bought=False
                if log :
                    transaction={ 
                        "Date":self.ohlcv_data.index[i],
                        "Instrument Symbol": instr,
                        "Transaction Type":"sell",
                        "Number of stocks": number_stocks,
                        "Buy Price":self.ohlcv_data[config.SELL_PRICE].iloc[i],
                        "solde":solde

                    }
                    print(transaction)
            


        if is_bought:
            solde+=(number_stocks*self.ohlcv_data[config.SELL_PRICE].iloc[i]) - self.get_tax(number_stocks* self.ohlcv_data[config.SELL_PRICE].iloc[i],config.TAX)
            if log :
                    transaction={ 
                        "Date":self.ohlcv_data.index[i],
                        "Instrument Symbol": instr,
                        "Transaction Type":"sell",
                        "Number of stocks": number_stocks,
                        "Buy Price":self.ohlcv_data[config.SELL_PRICE].iloc[i],
                        "solde":solde

                    }
                    print(transaction)
        if return_roi:
            roi=(solde-config.INITIAL_SOLDE)/config.INITIAL_SOLDE
            return roi

        return solde

        

 