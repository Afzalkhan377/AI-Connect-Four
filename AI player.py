#
# AI Player for use in Connect Four  
#

import random  
from moves import *

class AIPlayer(Player): 
    def  __init__(self, checker, tiebreak, lookahead):
            assert(checker == 'X' or checker == 'O')
            assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
            assert(lookahead >= 0)
            super().__init__(checker)
            
            self.tiebreak=tiebreak
            self.lookahead=lookahead
       
    def __repr__(self):
        """ returns a string with the checekre of the AI Player and look ahead number. 
        """    
        s= super().__repr__()
        s+= " (" + self.tiebreak + ", " +str(self.lookahead)+")"
        return s
       

    def max_score_column(self, scores):  
        """ makes a list of numbers at which ac checker can be added and returs a randomn numbr 
        """
        s=max(scores)
        c=[]

        for r in range(len(scores)):
            if scores[r]==s:
                c+=[r]
        if self.tiebreak=="LEFT":
            return c[0]
        elif self.tiebreak=="RIGHT":
            return c[-1]
        else:
            return random.choice(c)

    def scores_for(self, b):
        """ Produces a list of of number which indicate if you win, lose or its a tie.
            depedning on the look ahead the numbers differ.
        """
        scores=[0]*b.width
        for x in range (b.width):
            if b.can_add_to(x)==False:
                scores[x]=-1
            elif b.is_win_for(self.checker)==True:
                scores[x]=100
            elif b.is_win_for(self.opponent_checker())==True:
                scores[x]=0
            elif self.lookahead==0:
                scores[x]=50
        
            else:
                b.add_checker(self.checker, x)
                c=AIPlayer(self.opponent_checker(),self.tiebreak, self.lookahead-1)
                opp_scores= c.scores_for(b)
                scores[x]=opp_scores[x]
                if max(opp_scores)==0:
                    scores[x]=100
                elif max(opp_scores)==100:
                    scores[x]=0
                if max(opp_scores)==50:
                    scores[x]=50
                b.remove_checker(x)
        return scores
                
    def next_move(self, b):
        """ returns a column number where a checker is gonna be placed. 
        """
        self.num_moves+=1
        c= self.scores_for(b)
        column= self.max_score_column(c)
        return column
                
           
      
     