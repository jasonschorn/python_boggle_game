import time
import datetime
from Class_Board import Board
from Class_Positions import Positions

########################################################################################
# CLASS_WORDS
#
#
#   CLASS_PLAYER <--- CLASS_WORDS
#                     |         |
#                     |         |
#                     |         |
#              CLASS_BOARD   CLASS_POSITIONS
#                   |
#                   |
#                   |
#               CLASS_DICE
########################################################################################
class Words:

#    NUM_MINS = 1
#    END_TIME = datetime.datetime.now() + datetime.timedelta(minutes=NUM_MINS)

    def __init__(self) -> None:
        '''
            Words are unique to objects of CLASS_PERSON and all methods of type WORDS are called through a given person.
        '''
        self._list_of_words: list[str] = []


    @property
    def list_of_words(self) -> list[str]:
        return self._list_of_words
    
    @list_of_words.setter
    def list_of_words(self, word:str) -> None:
        self.list_of_words.append(word)


    def reset_list_of_words(self) -> None:
        '''
            Called from Player.reset_player() and uses LIST.clear() to remove all words from the list
        '''
        self.list_of_words.clear()


    def convert_positions_to_word(self, the_board:Board, the_positions:list[int]) -> str:
        '''
            For a given game board and list of user entered board positions, convert those
            integer positions into an English word
        '''
        the_word = ''
        for pos in the_positions:
            # Originally used get_row() and get_col() from CLASS_BOARD
            the_word += the_board.game_board[the_board.get_row_index(pos)][the_board.get_col_index(pos)]
        
        return the_word
    

    def collect_words(self, the_board:Board, end_time):
        '''
            Main driver for collecting user entered positions over a predetermined period of time 
            where each collection of positions correspond to letters on a given game board
            and subsequently spell a potentially valid English word.

            END_TIME is fixed during the start of a game and where END_TIME ranges from 
        '''
        the_positions = Positions()

        while True:
            if datetime.datetime.now() >= end_time:
                break
            else:
                the_positions.get_positions()
        
        for pos in the_positions.positions:
            self.list_of_words = self.convert_positions_to_word(the_board, pos)


    
###################################################################
# TEST 
###################################################################
""" w = Words()
b=Board()
b.print_board()
w.collect_words(b) """