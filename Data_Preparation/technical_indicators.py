import pandas as pd
import numpy as np
import talib
import sys
sys.path.append('C:/Users/Wael/Desktop/RoboTraderProject')

from config.config import USED_CLOSE_PRICE






"""
Extract technical indicators from prices 
"""



def Set_indicators(data,period):
    """
    :param data: dataframe containing ohlcv prices and indexed with date
    :param period: period used to calculate indicators
    :return: dataframe of Technical indicators of specefic timeframe

    """



    df=pd.DataFrame(index=data.index)
    df["mom"+str(period)]=talib.MOM(data[USED_CLOSE_PRICE], timeperiod=period)
    #change it later
    df["slowk"+str(period)],df["slowd"+str(period)]= talib.STOCH(data["High"], data["Low"], data[USED_CLOSE_PRICE], fastk_period=period, slowk_period=period, slowk_matype=0, slowd_period=period, slowd_matype=0)

    #WILLR
    df["willr"+str(period)]= talib.WILLR(data["High"], data["Low"], data[USED_CLOSE_PRICE], timeperiod=period)
     
    
    #MACDFIX - Moving Average Convergence/Divergence Fix 12/26
    df["macd"+str(period)], df["macdsignal"+str(period)], df["macdhist"+str(period)] = talib.MACDFIX(data[USED_CLOSE_PRICE], signalperiod=period)

    #CCI
    df["cci"+str(period)]= talib.CCI(data["High"], data["Low"], data[USED_CLOSE_PRICE], timeperiod=period)
    
    #Bollinger Bands
    df["upperband"+str(period)],df["middleband"+str(period)],df["lowerband"+str(period)]= talib.BBANDS(data[USED_CLOSE_PRICE], timeperiod=period, nbdevup=2, nbdevdn=2, matype=0)

    #HIGH SMA
    df["smaHigh"+str(period)]= talib.SMA(data["High"], timeperiod=period)
    
    # SMA Adj Prices
    df["sma"+str(period)]= talib.SMA(data[USED_CLOSE_PRICE], timeperiod=period)

    df["smaHighLow"+str(period)] = talib.SMA(talib.MEDPRICE(data["High"], data["Low"]), timeperiod=period)
    
    
    
    #DEMA - Double Exponential Moving Average
    df["DEMA"+str(period)] = talib.DEMA(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #EMA - Exponential Moving Average
    df["EMA"+str(period)] = talib.EMA(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
    df["HT_TRENDLINE"+str(period)] = talib.HT_TRENDLINE(data[USED_CLOSE_PRICE])
    
    #KAMA - Kaufman Adaptive Moving Average
    df["KAMA"+str(period)] = talib.KAMA(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #T3 - Triple Exponential Moving Average (T3)
    df["T3-"+str(period)] = talib.T3(data[USED_CLOSE_PRICE], timeperiod=period, vfactor=0)

    #TEMA - Triple Exponential Moving Average
    df["TEMA"+str(period)] = talib.TEMA(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #TRIMA - Triangular Moving Average
    df["TRIMA"+str(period)] = talib.TRIMA(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #WMA - Weighted Moving Average
    df["TRIMA"+str(period)] = talib.WMA(data[USED_CLOSE_PRICE], timeperiod=period)
    
    
    
    ##########
    
    
    
    #ADX - Average Directional Movement Index
    df["ADX"+str(period)] = talib.ADX(data["High"], data["Low"], data[USED_CLOSE_PRICE], timeperiod=period)
    
    #ADXR - Average Directional Movement Index Rating
    df["ADXR"+str(period)] = talib.ADXR(data["High"], data["Low"], data[USED_CLOSE_PRICE], timeperiod=period)
    
    #AROON - Aroon
    df["aroondown"+str(period)], df["aroonup"+str(period)] = talib.AROON(data["High"], data["Low"], timeperiod=period)
    
    #AROONOSC - Aroon Oscillator
    df["aroondown"+str(period)] = talib.AROONOSC(data["High"], data["Low"], timeperiod=period)
    

    
    
    #CMO - Chande Momentum Oscillator
    df["CMO"+str(period)] = talib.CMO(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #DX - Directional Movement Index
    df["DX"+str(period)]= talib.DX(data["High"], data["Low"], data[USED_CLOSE_PRICE], timeperiod=period)

    
    
    
    #MINUS_DI - Minus Directional Indicator
    df["MINUS_DI"+str(period)] = talib.MINUS_DI(data["High"], data["Low"], data[USED_CLOSE_PRICE], timeperiod=period)
    
    #MINUS_DM - Minus Directional Movement
    df["MINUS_DM"+str(period)] = talib.MINUS_DM(data["High"], data["Low"], timeperiod=period)
    
    #PLUS_DI - Plus Directional Indicator
    df["PLUS_DI"+str(period)] = talib.PLUS_DI(data["High"], data["Low"], data[USED_CLOSE_PRICE], timeperiod=period)

    #PLUS_DM - Plus Directional Movement
    df["PLUS_DM"+str(period)] = talib.PLUS_DM(data["High"], data["Low"], timeperiod=period)
    
    #ROC - Rate of change : ((price/prevPrice)-1)*100
    df["roc"+str(period)]=talib.ROC(data[USED_CLOSE_PRICE], timeperiod=period)

    #ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice
    df["ROCP"+str(period)] = talib.ROCP(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #ROCR - Rate of change ratio: (price/prevPrice)
    df["ROCR"+str(period)] = talib.ROCR(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100
    df["ROCR100-"+str(period)] = talib.ROCR100(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #RSI - Relative Strength Index
    df["RSI-"+str(period)] = talib.RSI(data[USED_CLOSE_PRICE], timeperiod=period)
    
    #TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    df["TRIX"+str(period)] = talib.TRIX(data[USED_CLOSE_PRICE], timeperiod=period)

    #MFI - Money Flow Index
    df["MFI"+str(period)] =talib.MFI(data["High"], data["Low"], data[USED_CLOSE_PRICE], data["Volume"], timeperiod=period)

    #ADOSC - Chaikin A/D Oscillator set periods later please
    df["ADOSC"+str(period)] =talib.ADOSC(data["High"], data["Low"], data[USED_CLOSE_PRICE], data["Volume"], fastperiod= np.round(period/3) , slowperiod=period)


    return df




def Set_multiple_timeframe_indicators(data,begin,end,verbose=True):
    """
    :param @data: dataframe containing ohlcv prices and indexed with date
    :param @begin: first timeframe used to calculate indicators
    :param @end: last timeframe used to calculate indicators
    :return: dataframe of Technical indicators of different timeframes from @begin to @end

    """
    if verbose:
        print("Extracting TA ...")

    df=pd.DataFrame(index=data.index)
    for timeframe in range(begin,end):
        d=Set_indicators(data,timeframe)
        df=pd.concat([df,d],axis=1,join='inner')

        if verbose:
            print(str(timeframe)+"timeframe TA done")


    #AD - Chaikin A/D Line
    df["AD"] =talib.AD(data["High"], data["Low"], data[USED_CLOSE_PRICE], data["Volume"])

    df["OBV"] =talib.OBV(data[USED_CLOSE_PRICE], data["Volume"])

    #BOP - Balance Of Power
    df["BOP"] = talib.BOP(data["Open"], data["High"], data["Low"], data[USED_CLOSE_PRICE])

    df["priceAvg"] = talib.AVGPRICE(data.Open, data["High"], data["Low"], data[USED_CLOSE_PRICE])

    #Adding date column
    df["Date"]=data["Date"]


    return df






