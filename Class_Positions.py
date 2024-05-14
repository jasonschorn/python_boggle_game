########################################################################################
# CLASS_
########################################################################################
class Positions:

    possible_paths = {1 : [2,5,6],
         2 : [1,3,5,6,7],
         3 : [2,4,6,7,8],
         4 : [3,7,8],
         5 : [1,2,6,9,10],
         6 : [1,2,3,5,7,9,10,11],
         7 : [2,3,4,6,8,10,11,12],
         8 : [3,4,7,11,12],
         9 : [5,6,10,13,14],
         10 : [5,6,7,9,11,13,14,15],
         11 : [6,7,8,10,12,14,15,16],
         12 : [7,8,11,15,16],
         13 : [9,10,14],
         14 : [9,10,11,13,15],
         15 : [10,11,12,14,16],
         16 : [11,12,15] }


    def __init__(self) -> None:
        self._positions = []


    @property
    def positions(self) -> list:
        return self._positions
    
    @positions.setter
    def positions(self, vals:list[int]) -> None:
        self.positions.append(vals)
    

    def clear_positions(self) -> None:
        self.positions.clear()


    def validate_in_range(self, the_positions:list[int]) -> bool:
        if all([val in range(1,17) for val in the_positions]):
            return True
        else:
            return False


    def validate_no_repitition(self, the_positions:list[int]) -> bool:
        return all([the_positions.count(item) == 1 for item in the_positions])

    ###############################################################################################################
    # A valid path is any choice of an available position within the at most 8-adjacent ring positions surrounding
    # a given position where each choice continues for the length of the assumed word and is such that the choice
    # does not repeat nor does is exist outside the range [1 - 16].
    #
    #
    #   EXAMPLE - from position 6 the avaiable path positions would lie in the set {1, 2, 3, 5, 7, 9, 10, 11}
    #
    #   | 1  | 2  | 3  |
    #   | 5  | 6  | 7  |
    #   | 9  | 10 | 11 |
    #
    #   Similarly, starting at position 16 the only available path poitions lie in the set {11, 12, 15}
    #
    #   | 11 | 12 |
    #   | 15 | 16 |
    ###############################################################################################################
    #def validate_path(self, the_positions: list) -> bool:
    #    return all([ abs(the_positions[i-1] - the_positions[i]) <= 5 for i in range(1, len(the_positions))])
    def validate_path(self, positions:list[int]) -> bool:
        for i in range(1, len(positions)):
            if not positions[i] in self.possible_paths[positions[i-1]]:
                return False
    
        return True


    def validate_positions(self, the_positions:list[int]) -> bool:
        # No repititions
        # if abs(pi - pj) > 5 then they are not adjacent
        # if abs(pi - pj) not in {1,3,4,5} then they are not adjacent
        return self.validate_no_repitition(the_positions) and self.validate_path(the_positions) and self.validate_in_range(the_positions)


    def get_positions(self) -> None:
            while True:
                try:
                    the_positions = [int(pos) for pos in input('Enter Positions: ').split(',')]
                except ValueError:
                    print('Invalid entry, please re-enter positons')
                else:
                    if self.validate_positions(the_positions):
                        self.positions = the_positions
                        break
                    else:
                        the_positions.clear()
                        print('Invlaid position(s) given')
