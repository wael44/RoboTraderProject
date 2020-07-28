from scipy import optimize
import pandas as pd
import sys
sys.path.append('C:/Users/Wael/Desktop/RoboTraderProject')


from db.get import *
from config import config



class Perfect_behaviour:
    def __init__(self,):
        self.ohlcv_data=None

    def find_perfect_behaviour(self,inst,start=None,end=None, verbose=True):
        """
            Find the best path in specefic instrument

            :param inst: the instrument symbol
            :param start: the start date 
            :param end: the end date
            :return: a tuple of dataframe containing the best path (indexed with date) and the gain of that path
        """
        #Get daily data
        if(start !=None and end!= None):
            self.ohlcv_data= pd.DataFrame(get_ohlcv(inst,start=start,end=end))
            self.ohlcv_data.set_index("Date",inplace=True)
        else:
            self.ohlcv_data=pd.DataFrame(get_ohlcv(inst))
            self.ohlcv_data.set_index("Date",inplace=True)

        
        #test delete it later
        self.ohlcv_data=self.ohlcv_data.iloc[-100:]
        ########################################

        #list of tuples, every tuples contain the perfect behaviour for a segment
        perfect_behaviour_tuples=[]

        #running the differential evolution algorithm on big dataset take long time, so we split the dataset into segments.
        #each segment size is config.GA_SEGMENT_SIZE. to get the number of segments we divise the dataset size by the segment size
        number_segments=round(self.ohlcv_data.shape[0]/config.GA_SEGMENT_SIZE)

        for segment in range(number_segments):
            segment_indice=segment*config.GA_SEGMENT_SIZE

            if verbose:
                print("Segment "+str(segment+1)+" of "+ str(number_segments)+" segments...")

            
            #due to the stochastic nature of the differential evolution algorithm, the algorithm may find different solution for every iteration
            #So we try to run the algorithm a number of times (GA_ITERATIONS_PER_SEGMENT iterations) for every segment and take the best solution
            perfect_behaviour_segment=[] 
            for iter in range(config.GA_ITERATIONS_PER_SEGMENT):
                if verbose:
                    print("Iteration "+str(iter+1)+" of Segment" +str(segment+1))
                if (segment+1==number_segments): #if the last segment then take the rested elements
                    perfect_behaviour_segment.append(self.differential_evolution(self.ohlcv_data.iloc[segment_indice:]))    
                else:
                    perfect_behaviour_segment.append(self.differential_evolution(self.ohlcv_data.iloc[segment_indice:segment_indice+config.GA_SEGMENT_SIZE]))
            
            #take the best solution
            perfect_behaviour_tuples.append(self.get_best_solution(perfect_behaviour_segment))


        
        #Convert the list of tuples to list containing the solution
        perfect_behaviour = [perfect_behaviour_tuple[0] for perfect_behaviour_tuple in perfect_behaviour_tuples] #the result is a list of lists (each list is the solution for each segment)
        perfect_behaviour = [y for x in perfect_behaviour for y in x] #convert the list of lists to one list

        #the total gain resulted on the found solution
        gain = sum([(perfect_behaviour_tuple[1]-config.INITIAL_SOLDE) for perfect_behaviour_tuple in perfect_behaviour_tuples])

        df=pd.DataFrame(index=self.ohlcv_data.index)
        
        df["decision"]=perfect_behaviour

        return df , gain 
        




    def differential_evolution(self,data):
        bounds = [(-1,1) for _ in range(data.shape[0])]
        #perfect_behaviouris a result object that have two attributes : 1)x : the solution array 2)fun: the value resulted of solution
        perfect_behaviour= optimize.differential_evolution(self.simulator , bounds=bounds ,disp=True , workers=-1 )
        perfect_behaviour.x = [round(x) for x in perfect_behaviour.x ]
        return (perfect_behaviour.x, abs(perfect_behaviour.fun))


    def get_best_solution(self,segments):
        """
            :param segments: list of tuples.the first element of tuple contains solution and the second element contains the result for that solution
            :return: tuple that contain the best result
        """
        #get the segment that have the best gain || the structure of the tuples { (list contains solution,result) }
        return max(segments,key=lambda item:item[1])




    def get_tax(self,price,tax_rate):
        return price*tax_rate/100


    def simulator(self,X):

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
            elif(decision==-1 and is_bought):
                solde+=(number_stocks*self.ohlcv_data[config.SELL_PRICE].iloc[i]) - self.get_tax(number_stocks* self.ohlcv_data[config.SELL_PRICE].iloc[i],config.TAX)
                is_bought=False
            
            elif((decision==1 and  is_bought) or (decision==-1 and not is_bought)): #Imposing a penalty to randomly generated decisions to force the GA to change them

                solde-=config.GA_SEGMENT_SIZE

        if is_bought:
            solde+=(number_stocks*self.ohlcv_data[config.SELL_PRICE].iloc[i]) - self.get_tax(number_stocks* self.ohlcv_data[config.SELL_PRICE].iloc[i],config.TAX)

        return -solde
    

