from . import db
import pandas as pd
from datetime import datetime

def get_ohlcv(inst,start=None,end=None,transform_to_dataframe=False):
    """
        :param inst: Name of the instrument
        :param start: start date
        :param end: end date
        :param transform_to_dataframe: if true , the result will be transformed to dataframe, else it will be a list of dictionaries
        :return: ohlcv data of the instrument (list of dictionaries) [if transform_to_dataframe is set to True the function will return a dataframe]
    """

    #get the collection context
    collection = db[inst]

    #if no start and end dates are setted then return all avaible data
    if(start==None and end == None ):
        result=list(collection.find({},{"_id":0}).sort('Date' , 1))
        if transform_to_dataframe:
            return pd.DataFrame(result)
        return result
    elif (end == None):
        end = datetime(2025,12,31)
    

    query={}
    #set the start and end date in the query
    query['Date'] = {'$gte' : start , '$lt' : end }
    
    result =list(collection.find(query,{"_id":0}).sort('Date' , 1))

    if transform_to_dataframe:
            return pd.DataFrame(result)
    return result





def get_last_ohlcv(inst):
    """
        :param inst: Name of the instrument
        :return: last day ohlcv data of the instrument
    """
    #get the collection context
    collection = db[inst]
    result=list(collection.find({},{"_id":0}).sort('Date' , 1))

    #To do how to return last data
    return result


def get_intruments_names(verbose=True):
    """
        Get the instruments names and symbols
        :return: dictionarie containing instrument name indexed by its symbol (EXEMPLE : {'AC': 'Accor SA', 'ACA': 'Crédit Agricole S.A.'}) 
    """
    collection = db["Instruments"]

    #collection.find({},{"_id":0}) return a list of dictionaries that contains instruments symbol and name ( [{'symbol': 'AC', 'Instrument_name': 'Accor SA'}, {'symbol': 'ACA', 'Instrument_name': 'Crédit Agricole S.A.'}])
    #transform that list to a dictionarie
    if verbose:
        print("getting instruments names...")
    res={d["symbol"]:d["Instrument_name"] for d in collection.find({},{"_id":0})}
    if verbose:
        if (res!={}) :
            print("done")
        else:
            print("an error occurred")
    return res



def get_ta(instr,start=None,end=None,transform_to_dataframe=False):
    """
        :param inst: Name of the instrument
        :param start: start date
        :param end: end date
        :return: TA data of the instrument (list of dictionaries)
    """

    #get the collection context
    collection = db[instr+"_TA"]

    #if no start and end dates are setted then return all available data
    if(start==None and end == None ):
        result=list(collection.find({},{"_id":0})) #.sort('Date' , 1))
        if transform_to_dataframe:
            return pd.DataFrame(result)
        return result
    elif (end == None):
        end = datetime(2025,12,31)

    query={}
    #set the start and end date in the query
    query['Date'] = {'$gte' : start , '$lt' : end }
    
    result =list(collection.find(query,{"_id":0}) )#.sort('Date' , 1))
    if transform_to_dataframe:
            return pd.DataFrame(result)
    return result



def get_slopes(instr,start=None,end=None,transform_to_dataframe=False):
    """
        :param inst: Name of the instrument
        :param start: start date
        :param end: end date
        :return: TA data of the instrument (list of dictionaries)
    """

    #get the collection context
    collection = db[instr+"_Slopes"]

    #if no start and end dates are setted then return all available data
    if(start==None and end == None ):
        result=list(collection.find({},{"_id":0}).sort('Date' , 1))
        if transform_to_dataframe:
            return pd.DataFrame(result)
        return result
    elif (end == None):
        end = datetime(2025,12,31)

    query={}
    #set the start and end date in the query
    query['Date'] = {'$gte' : start , '$lt' : end }
    
    result =list(collection.find(query,{"_id":0}).sort('Date' , 1))
    if transform_to_dataframe:
            return pd.DataFrame(result)
    return result