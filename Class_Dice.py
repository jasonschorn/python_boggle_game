from random import randint


########################################################################################
# CLASS_
########################################################################################
class Dice:

    boggle_classic = {1: ['A', 'A', 'C', 'I', 'O', 'T'], 
                       2: ['A', 'B', 'I', 'L', 'T', 'Y'], 
                       3: ['A', 'B', 'J', 'M', 'O', 'Qu'], 
                       4: ['A', 'C', 'D', 'E', 'M', 'P'], 
                       5: ['A', 'C', 'E', 'L', 'R', 'S'], 
                       6: ['A', 'D', 'E', 'N', 'V', 'Z'], 
                       7: ['A', 'H', 'M', 'O', 'R', 'S'], 
                       8: ['B', 'I', 'F', 'O', 'R', 'X'], 
                       9: ['D', 'E', 'N', 'O', 'S', 'W'], 
                       10: ['D', 'K', 'N', 'O', 'T', 'U'], 
                       11: ['E', 'E', 'F', 'H', 'I', 'Y'], 
                       12: ['E', 'G', 'K', 'L', 'U', 'Y'], 
                       13: ['E', 'G', 'I', 'N', 'T', 'V'], 
                       14: ['E', 'H', 'I', 'N', 'P', 'S'], 
                       15: ['E', 'L', 'P', 'S', 'T', 'U'], 
                       16: ['G', 'I', 'L', 'R', 'U', 'W']}

    boggle_new = {1: ['A', 'A', 'E', 'E', 'G', 'N'], 
                    2: ['A', 'B', 'B', 'J', 'O', 'O'], 
                    3: ['A', 'C', 'H', 'O', 'P', 'S'], 
                    4: ['A', 'F', 'F', 'K', 'P', 'S'], 
                    5: ['A', 'O', 'O', 'T', 'T', 'W'], 
                    6: ['C', 'I', 'M', 'O', 'T', 'U'], 
                    7: ['D', 'E', 'I', 'L', 'R', 'X'], 
                    8: ['D', 'E', 'L', 'R', 'V', 'Y'], 
                    9: ['D', 'I', 'S', 'T', 'T', 'Y'], 
                    10: ['E', 'E', 'G', 'H', 'N', 'W'], 
                    11: ['E', 'E', 'I', 'N', 'S', 'U'], 
                    12: ['E', 'H', 'R', 'T', 'V', 'W'], 
                    13: ['E', 'I', 'O', 'S', 'S', 'T'], 
                    14: ['E', 'L', 'R', 'T', 'T', 'Y'], 
                    15: ['H', 'I', 'M', 'N', 'U', 'Qu'], 
                    16: ['H', 'L', 'N', 'N', 'R', 'Z']}

    boggle_big_original = {1: ['A', 'A', 'A', 'F', 'R', 'S'], 
                                2: ['A', 'A', 'E', 'E', 'E', 'E'], 
                                3: ['A', 'A', 'F', 'I', 'R', 'S'], 
                                4: ['A', 'D', 'E', 'N', 'N', 'N'], 
                                5: ['A', 'E', 'E', 'E', 'E', 'M'], 
                                6: ['A', 'E', 'E', 'G', 'M', 'U'], 
                                7: ['A', 'E', 'G', 'M', 'N', 'N'], 
                                8: ['A', 'F', 'I', 'R', 'S', 'Y'], 
                                9: ['B', 'J', 'K', 'Qu', 'X', 'Z'], 
                                10: ['C', 'C', 'E', 'N', 'S', 'T'], 
                                11: ['C', 'E', 'I', 'I', 'L', 'T'], 
                                12: ['C', 'E', 'I', 'P', 'S', 'T'], 
                                13: ['D', 'D', 'H', 'N', 'O', 'T'], 
                                14: ['D', 'H', 'H', 'L', 'O', 'R'], 
                                15: ['D', 'H', 'H', 'L', 'O', 'R'], 
                                16: ['D', 'H', 'L', 'N', 'O', 'R'], 
                                17: ['E', 'I', 'I', 'I', 'T', 'T'], 
                                18: ['C', 'E', 'I', 'L', 'P', 'T'], 
                                19: ['E', 'M', 'O', 'T', 'T', 'T'], 
                                20: ['E', 'N', 'S', 'S', 'S', 'U'], 
                                21: ['F', 'I', 'P', 'R', 'S', 'Y'], 
                                22: ['G', 'O', 'R', 'R', 'V', 'W'], 
                                23: ['I', 'P', 'R', 'R', 'R', 'Y'], 
                                24: ['N', 'O', 'O', 'T', 'U', 'W'], 
                                25: ['O', 'O', 'O', 'T', 'T', 'U']}

    boggle_big_challenge = {1: ['A', 'A', 'A', 'F', 'R', 'S'], 
                                2: ['A', 'A', 'E', 'E', 'E', 'E'], 
                                3: ['A', 'A', 'F', 'I', 'R', 'S'], 
                                4: ['A', 'D', 'E', 'N', 'N', 'N'], 
                                5: ['A', 'E', 'E', 'E', 'E', 'M'], 
                                6: ['A', 'E', 'E', 'G', 'M', 'U'], 
                                7: ['A', 'E', 'G', 'M', 'N', 'N'], 
                                8: ['A', 'F', 'I', 'R', 'S', 'Y'], 
                                9: ['B', 'J', 'K', 'Qu', 'X', 'Z'], 
                                10: ['C', 'C', 'E', 'N', 'S', 'T'], 
                                11: ['C', 'E', 'I', 'I', 'L', 'T'], 
                                12: ['C', 'E', 'I', 'P', 'S', 'T'], 
                                13: ['D', 'D', 'H', 'N', 'O', 'T'], 
                                14: ['D', 'H', 'H', 'L', 'O', 'R'], 
                                15: ['I', 'K', 'L', 'M', 'Qu', 'U'], 
                                16: ['D', 'H', 'L', 'N', 'O', 'R'], 
                                17: ['E', 'I', 'I', 'I', 'T', 'T'], 
                                18: ['C', 'E', 'I', 'L', 'P', 'T'], 
                                19: ['E', 'M', 'O', 'T', 'T', 'T'], 
                                20: ['E', 'N', 'S', 'S', 'S', 'U'], 
                                21: ['F', 'I', 'P', 'R', 'S', 'Y'], 
                                22: ['G', 'O', 'R', 'R', 'V', 'W'], 
                                23: ['I', 'P', 'R', 'R', 'R', 'Y'], 
                                24: ['N', 'O', 'O', 'T', 'U', 'W'], 
                                25: ['O', 'O', 'O', 'T', 'T', 'U']}

    boggle_big_deluxe = {1: ['A', 'A', 'A', 'F', 'R', 'S'], 
                            2: ['A', 'A', 'E', 'E', 'E', 'E'], 
                            3: ['A', 'A', 'F', 'I', 'R', 'S'], 
                            4: ['A', 'D', 'E', 'N', 'N', 'N'], 
                            5: ['A', 'E', 'E', 'E', 'E', 'M'], 
                            6: ['A', 'E', 'E', 'G', 'M', 'U'], 
                            7: ['A', 'E', 'G', 'M', 'N', 'N'], 
                            8: ['A', 'F', 'I', 'R', 'S', 'Y'], 
                            9: ['B', 'J', 'K', 'Qu', 'X', 'Z'], 
                            10: ['C', 'C', 'N', 'S', 'T', 'W'], 
                            11: ['C', 'E', 'I', 'I', 'L', 'T'], 
                            12: ['C', 'E', 'I', 'P', 'S', 'T'], 
                            13: ['D', 'D', 'L', 'N', 'O', 'R'], 
                            14: ['D', 'H', 'H', 'L', 'O', 'R'], 
                            15: ['D', 'H', 'H', 'N', 'O', 'T'], 
                            16: ['D', 'H', 'L', 'N', 'O', 'R'], 
                            17: ['E', 'I', 'I', 'I', 'T', 'T'], 
                            18: ['C', 'E', 'I', 'L', 'P', 'T'], 
                            19: ['E', 'M', 'O', 'T', 'T', 'T'], 
                            20: ['E', 'N', 'S', 'S', 'S', 'U'], 
                            21: ['F', 'I', 'P', 'R', 'S', 'Y'], 
                            22: ['G', 'O', 'R', 'R', 'V', 'W'], 
                            23: ['H', 'I', 'P', 'R', 'R', 'Y'], 
                            24: ['N', 'O', 'O', 'T', 'U', 'W'], 
                            25: ['O', 'O', 'O', 'T', 'T', 'U']}

    boggle_big_2012 = {1: ['A', 'A', 'A', 'F', 'R', 'S'], 
                            2: ['A', 'A', 'E', 'E', 'E', 'E'], 
                            3: ['A', 'A', 'F', 'I', 'R', 'S'], 
                            4: ['A', 'D', 'E', 'N', 'N', 'N'], 
                            5: ['A', 'E', 'E', 'E', 'E', 'M'], 
                            6: ['A', 'E', 'E', 'G', 'M', 'U'], 
                            7: ['A', 'E', 'G', 'M', 'N', 'N'], 
                            8: ['A', 'F', 'I', 'R', 'S', 'Y'], 
                            9: ['B', 'B', 'J', 'K', 'X', 'Z'], 
                            10: ['C', 'C', 'E', 'N', 'S', 'T'], 
                            11: ['E', 'I', 'I', 'L', 'S', 'T'], 
                            12: ['C', 'E', 'I', 'P', 'S', 'T'], 
                            13: ['D', 'D', 'H', 'N', 'O', 'T'], 
                            14: ['D', 'H', 'H', 'L', 'O', 'R'], 
                            15: ['D', 'H', 'H', 'N', 'O', 'W'], 
                            16: ['D', 'H', 'L', 'N', 'O', 'R'], 
                            17: ['E', 'I', 'I', 'I', 'T', 'T'], 
                            18: ['E', 'I', 'L', 'P', 'S', 'T'], 
                            19: ['E', 'M', 'O', 'T', 'T', 'T'], 
                            20: ['E', 'N', 'S', 'S', 'S', 'U'], 
                            21: ['Qu', 'In', 'Th', 'Er', 'He', 'An'], 
                            22: ['G', 'O', 'R', 'R', 'V', 'W'], 
                            23: ['I', 'P', 'R', 'S', 'Y', 'Y'], 
                            24: ['N', 'O', 'O', 'T', 'U', 'W'], 
                            25: ['O', 'O', 'O', 'T', 'T', 'U']}

    boggle_super_big = {1: ['A', 'A', 'A', 'F', 'R', 'S'], 
                            2: ['A', 'A', 'E', 'E', 'E', 'E'], 
                            3: ['A', 'A', 'E', 'E', 'O', 'O'], 
                            4: ['A', 'A', 'F', 'I', 'R', 'S'], 
                            5: ['A', 'B', 'D', 'E', 'I', 'O'], 
                            6: ['A', 'D', 'E', 'N', 'N', 'N'], 
                            7: ['A', 'E', 'E', 'E', 'E', 'M'], 
                            8: ['A', 'E', 'E', 'G', 'M', 'U'], 
                            9: ['A', 'E', 'G', 'M', 'N', 'N'], 
                            10: ['A', 'E', 'I', 'L', 'M', 'N'], 
                            11: ['A', 'E', 'I', 'N', 'O', 'U'], 
                            12: ['A', 'F', 'I', 'R', 'S', 'Y'], 
                            13: ['Qu', 'In', 'Th', 'Er', 'He', 'An'], 
                            14: ['B', 'B', 'J', 'K', 'X', 'Z'], 
                            15: ['C', 'C', 'E', 'N', 'S', 'T'], 
                            16: ['C', 'D', 'D', 'L', 'N', 'N'], 
                            17: ['C', 'E', 'I', 'I', 'T', 'T'], 
                            18: ['C', 'E', 'I', 'P', 'S', 'T'], 
                            19: ['C', 'F', 'G', 'N', 'U', 'Y'], 
                            20: ['D', 'D', 'H', 'N', 'O', 'T'], 
                            21: ['D', 'H', 'H', 'L', 'O', 'R'], 
                            22: ['D', 'H', 'H', 'N', 'O', 'W'], 
                            23: ['D', 'H', 'L', 'N', 'O', 'R'], 
                            24: ['E', 'H', 'I', 'L', 'R', 'S'], 
                            25: ['E', 'I', 'I', 'L', 'S', 'T'], 
                            26: ['E', 'I', 'L', 'P', 'S', 'T'], 
                            27: ['E', 'I', 'O', ' ', ' ', ' '], 
                            28: ['E', 'M', 'T', 'T', 'T', 'O'], 
                            29: ['E', 'N', 'S', 'S', 'S', 'U'], 
                            30: ['G', 'O', 'R', 'R', 'V', 'W'], 
                            31: ['H', 'I', 'R', 'S', 'T', 'V'], 
                            32: ['H', 'O', 'P', 'R', 'S', 'T'], 
                            33: ['I', 'P', 'R', 'S', 'Y', 'Y'], 
                            34: ['J', 'K', 'Qu', 'W', 'X', 'Z'], 
                            35: ['N', 'O', 'O', 'T', 'U', 'W'], 
                            36: ['O', 'O', 'O', 'T', 'T', 'U']}
    
    def __init__(self, game_type:str = 'Classic 4x4') -> None:
        if game_type == 'Classic 4x4':
            self._dice = [val[randint(0,5)] for val in self.boggle_classic.values()]
            self._rows = 4
            self._cols = 4
        
        elif game_type == 'New 4x4':
            self._dice = [val[randint(0,5)] for val in self.boggle_new.values()]
            self._rows = 4
            self._cols = 4
        
        elif game_type == 'Original 5x5':
            self._dice = [val[randint(0,5)] for val in self.boggle_big_original.values()]
            self._rows = 5
            self._cols = 5
        
        elif game_type == 'Challenge 5x5':
            self._dice = [val[randint(0,5)] for val in self.boggle_big_challenge.values()]
            self._rows = 5
            self._cols = 5
        
        elif game_type == 'Deluxe 5x5':
            self._dice = [val[randint(0,5)] for val in self.boggle_big_deluxe.values()]
            self._rows = 5
            self._cols = 5
        
        elif game_type == 'New 2012 5x5':
            self._dice = [val[randint(0,5)] for val in self.boggle_big_2012.values()]
            self._rows = 5
            self._cols = 5
        
        elif game_type == 'Super 6x6':
            self._dice = [val[randint(0,5)] for val in self.boggle_super_big.values()]
            self._rows = 6
            self._cols = 6
    

    @property
    def dice(self) -> list:
        return self._dice
    
    @property
    def rows(self) -> int:
        return self._rows
    
    @property
    def cols(self) -> int:
        return self._cols
