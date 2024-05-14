from Class_Dice import Dice


########################################################################################
# CLASS_BOARD
#
#   A Boggle game board consists of a <BOARD_ROWS> x <BOARD_COLS> grid of dice 
#   A standard game consists of a 4x4 matrix.  You can alter the variables
#   BOARD_ROWS and BOARD_COLS to adjust the game board as you see fit with the 
#   understanding that a larger board necessarily increases potential for finding
#   more words.  Of course, you will have to implement the additional dice. 
#
#
#   The class contructor performs the following:
#
#       (1) Calls the Dice contructor which returns a list of 16 randonly chosen strings
#           that represent 1 or the possible 6 faces of each Boggle die.
#       (2) Calls the internal function SELF.POPULATE_GAME_BOARD that creates the
#           4x4 game board
#
#
#   Origianl design was the use of a list of 4 lists but, this inhibits the ability
#   for future expansion of board size (See POPULATE_GAME_BOARD)
#
########################################################################################
class Board:
    
    BOARD_ROWS = 0
    BOARD_COLS = 0

    def __init__(self, the_dice:Dice) -> None:
        self.the_dice = the_dice
        self._game_board = self.populate_game_board()
        self._list_of_board_positions = [k+1 for k in range(self.the_dice.rows * self.the_dice.cols)]
        #self._list_of_board_positions = [k+1 for k in range(self.BOARD_ROWS * self.BOARD_COLS)]
    
    @property
    def game_board(self):
        return self._game_board
    
    @property
    def list_of_board_positions(self):
        return self._list_of_board_positions
    
    def set_rows(self):
        return self.the_dice.rows
    
    def set_cols(self):
        return self.the_dice.cols

    def populate_game_board(self) -> list:
        '''
            RETURNS and list of BOARD_COLS many lists containing ROWSxCOLS many objects of type Dice
        '''
        the_board = [[] for i in range(self.the_dice.cols)]
        counter = 0

        for row in range(self.the_dice.rows):
            for col in range(self.the_dice.cols):
                the_board[row].append(self.the_dice.dice[counter])
                counter += 1

        return the_board


    def generate_list_row_positions(self) -> list:
        return [self.list_of_board_positions[i:i+self.the_dice.rows] for i in range(0, len(self.list_of_board_positions), self.the_dice.rows)]


    def generate_list_col_positions(self) -> list:
        return [self.list_of_board_positions[i::5] for i in range(5)]

    
    def get_row_index(self, pos:int) -> int:
        rows = self.generate_list_row_positions()

        for index in range(self.the_dice.rows):
            if pos in rows[index]: 
                return index

    def get_col_index(self, pos:int) -> int:
        cols = self.generate_list_col_positions()

        for index in range(self.the_dice.cols):
            if pos in cols[index]:
                return index

    #
    #   USED IN CLASS_WORD  --->  CONVERT_POS_TO_WORD()
    #
    def get_row(self, the_position:int) -> int:
        if the_position in [1,2,3,4]:
            return 0
        elif the_position in [5,6,7,8]:
            return 1
        elif the_position in [9,10,11,12]:
            return 2
        else:
            return 3


    def get_col(self, the_position:int) -> int:
        if the_position in [1,5,9,13]:
            return 0
        elif the_position in [2,6,10,14]:
            return 1
        elif the_position in [3,7,11,15]:
            return 2
        else:
            return 3


    def get_row_positions_as_list_of_strings(self) -> list[str]:
        return [list(map(str, lst)) for lst in self.generate_list_row_positions()]


    def print_board_positions(self) -> None:
        string_pos = self.get_row_positions_as_list_of_strings()

        print('Positions:')
        for row in string_pos:
            print('|', end='')
            for col in row:
                if len(col) == 1:
                    print(f'  {col} |', end='')
                else:
                    print(f' {col} |', end='')
            print()
        print()


    def print_board(self) -> None:
        self.print_board_positions()
        print('Board: ')

        for row in self.game_board:
            print('|', end='')
            for col in row:
                if col in ['Qu', 'In', 'Th', 'Er', 'He', 'An']:
                    print(f' {col}|', end='')
                elif col == ' ':
                    print(f'   |', end='')
                else:
                    print(f' {col} |', end='')
            print()
        print()

d = Dice('Super 6x6')
b = Board(d)
b.print_board()
'''
    def print_standard_board_positions(self) -> None:
        print('Positions: ')
        print('|  1 |  2 |  3 |  4 |\n|  5 |  6 |  7 |  8 |\n|  9 | 10 | 11 | 12 |\n| 13 | 14 | 15 | 16 |\n')


    def print_big_board_positions(self) -> None:
        print('Positions: ')
        print('|  1 |  2 |  3 |  4 |  5 |\n|  6 |  7 |  8 |  9 | 10 |\n| 11 | 12 | 13 | 14 | 15 |\n| 16 | 17 | 18 | 19 | 20 |\n| 21 | 22 | 23 | 24 | 25 |\n')


    def print_super_big_board_positions(self) -> None:
        print('Positions: ')
        print('|  1 |  2 |  3 |  4 |  5 |  6 |\n|  7 |  8 |  9 | 10 | 11 | 12 |\n| 13 | 14 | 15 | 16 | 17 | 18 |\n| 19 | 20 | 21 | 2 | 23 | 24 |\n| 25 | 26 | 27 | 28 | 29 | 30 |\n| 31 | 32 | 33 | 34 | 35 | 36 |\n')
'''        