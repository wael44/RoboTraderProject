from datetime import datetime










#Path of dataset (csv files)
DATASET_PATH="Data_Aquisition\Datasets"


#Closed prices used in technical analysis and/or simulator (it can be "Adj Close" or "Close")
USED_CLOSE_PRICE="Adj Close"

#tax on each transaction
TAX=0.5
INITIAL_SOLDE=10000

SELL_PRICE="Low"
BUY_PRICE="High"


#Parameters for genetic algorithm
GA_SEGMENT_SIZE=50
GA_ITERATIONS_PER_SEGMENT=3

#Parameter for trend
NUMBER_TRESHS=100