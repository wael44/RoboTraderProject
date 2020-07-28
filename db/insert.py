from . import db
import pandas as pd
import sys
sys.path.append('C:/Users/Wael/Desktop/RoboTraderProject')


from Utilities.utilities import get_instr_name



def insert_ohlcv(inst,data,verbose=True):
    """
        :param inst: Name of the instrument
        :param data: DataFrame containing date,open,high,low,close,adjusted close and volume ||| IT MUST CONTAIN A COLUMN FOR DATE
        :return:
    """
    
    #Get the collection context, if the collection does not exist it will create it
    collection = db[inst]

    #Create index (to do)
    #collection.createIndex({'Date':1})

    #Convert DataFrame to List of Dictionaries
    docs=list(data.T.to_dict().values())

    if verbose:
        print("adding "+inst+" to database...")
    #insert the data
    collection.insert_many(docs)
    if verbose:
        print(inst+" added to database")

def insert_ta(inst,data,verbose=True):
    """
        :param inst: Name of the instrument
        :param data: DataFrame containing date,open,high,low,close,adjusted close and volume ||| IT MUST CONTAIN A COLUMN FOR DATE
        :return:
    """
    
    #Get the collection context, if the collection does not exist it will create it
    collection = db[inst+"_TA"]

    #Convert DataFrame to List of Dictionaries
    docs=list(data.T.to_dict().values())

    if verbose:
        print("adding "+inst+" TA to database...")
    #insert the data
    collection.insert_many(docs)
    if verbose:
        print(inst+" TA added to database")


def insert_perfect_behaviour_targets(inst,data,verbose=True):
    """
        :param inst: Name of the instrument
        :param data: DataFrame containing date, perfect path (serie of -1,0,1) ||| IT MUST CONTAIN A COLUMN FOR DATE
        :return:
    """
    
    #Get the collection context, if the collection does not exist it will create it
    collection = db[inst+"_PERFECT_BEHAVIOUR_TARGETS"]

    #Convert DataFrame to List of Dictionaries
    docs=list(data.T.to_dict().values())

    if verbose:
        print("adding "+inst+" PERFECT BEHAVIOUR TARGETS to database...")
    #insert the data
    collection.insert_many(docs)
    if verbose:
        print(inst+" PERFECT BEHAVIOUR TARGETS added to database")


def insert_slopes(inst,data,verbose=True):
    """
        :param inst: Name of the instrument
        :param data: DataFrame containing date, perfect path (serie of -1,0,1) ||| IT MUST CONTAIN A COLUMN FOR DATE
        :return:
    """

    #Get the collection context, if the collection does not exist it will create it
    collection = db[inst+"_Slopes"]

    #Convert DataFrame to List of Dictionaries
    docs=list(data.T.to_dict().values())

    if verbose:
        print("adding "+inst+" Slopes to database...")
    #insert the data
    collection.insert_many(docs)
    if verbose:
        print(inst+" Slopes added to database")



def insert_best_thresh(inst,data,verbose=True):
    """
        :param inst: Name of the instrument
        :param data: Dictionarie contains best thresh for up trend, best thresh for down trend and the gain
        :return:
    """
    
    #Get the collection context, if the collection does not exist it will create it
    collection = db["Thresh"]

    #Convert DataFrame to List of Dictionaries
    

    if verbose:
        print("adding "+inst+" Thresh to database...")
    #insert the data
    collection.insert_many(data)
    if verbose:
        print(inst+" Thresh added to database")





def insert_instruments_names(symbol):
    """
        :param symbol: symbol of the instrument
    """
    #get the collection context
    collection = db["Instruments"]

    #get the name of the instrument by its symbol
    doc={"symbol":symbol,"Instrument_name":get_instr_name(symbol)}

    #insert the doc 
    collection.insert_one(doc)