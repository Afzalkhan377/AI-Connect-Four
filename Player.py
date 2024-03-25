#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    """ a data type for a Connect Four player 
    """ 
    def __init__(self,checker):
        assert(checker == 'X' or checker == 'O')
        self.checker=checker
        self.num_moves=0
        
    def __repr__(self):
        """ return a string that shows the what checker the player is. 
        """
        s= "Player" + " " + self.checker
        return s
    
    
    def opponent_checker(self) :
        """ checks what checker is the opponent by checking the player's checker. 
        """
        if self.checker=="X":
            return "O"
        if self.checker== "O":
            return"X"
    
    def next_move(self, b):
        """ asks the player to where he wants to place the checker.
        """
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col)==True:
                return col

            else:
                print("Try again")
    