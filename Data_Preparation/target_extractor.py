import pandas as pd
import numpy as np
import talib

import sys
sys.path.append('C:/Users/Wael/Desktop/RoboTraderProject')

from db.get import *
from db.insert import *
from perfect_behaviour import Perfect_behaviour


"""
Difining Targets and save them to database
"""
#get intruments names from database (dictionarie containing instrument name indexed by its symbol (EXEMPLE : {'AC': 'Accor SA', 'ACA': 'Crédit Agricole S.A.'}) )
intruments_names=get_intruments_names()

#Perfect Behaviour Targets
for instr_name in intruments_names.keys():
    
    #Find the perfect behaviour 
    perfect_behaviour_targets=Perfect_behaviour().find_perfect_behaviour(str(instr_name))[0] #the find_perfect_behaviour function will return a tuple of dataframe containing the perfect path and the gain of that path.
                                                                                             #here we just need the perfect path so we took the first element

    perfect_behaviour_targets["Date"]=perfect_behaviour_targets.index #we need a column for date to add it to database
    #Saving Perfect Behaviour Targets to database
    insert_perfect_behaviour_targets(str(instr_name),perfect_behaviour_targets)



#Trend Targets
    






