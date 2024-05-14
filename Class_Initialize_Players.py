from Class_Player import Player


########################################################################################
# CLASS_
########################################################################################
class Initialize_Players:

    NUM_PLAYERS:int

    def __init__(self, score_for_kids) -> None:
        self._players: list[Player] = []
        self.score_for_kids = score_for_kids


    @property
    def players(self) -> list[Player]:
        return self._players
    
    @players.setter
    def players(self, the_player:Player) -> None:
        self._players.append(the_player)
    

    def show_players(self) -> None:
        for the_player in range(self.NUM_PLAYERS):
            print(self.players[the_player].name)
    

    def get_number_of_players(self) -> int:
        while True:
            try:
                num_players = int(input('\nEnter the number of players [1-6]: '))
            except ValueError:
                print('\nPlease enter a valid integer')
            else:
                if 1<= num_players <= 6:
                    self.NUM_PLAYERS = num_players
                    break
                else:
                    print('\nPlease enter a number between 1 and 6')
    


    def get_players_names(self) -> list:
        the_names = {}
        correct_names = ''
        
        while correct_names != 'y':
            if self.score_for_kids:
                for index in range(self.NUM_PLAYERS):
                    name = input(f'\nEnter a name for player #{index + 1}: ')

                    while True:
                        is_kid = input(f'Is this player a kids [Y/N]: ').lower()
            
                        if is_kid == 'y':
                            the_names[name] = True
                            break
                        elif is_kid == 'n':
                            the_names[name] = False
                            break
                        else:
                            print('\nPlease enter Y=Yes or N=No\n')
            else:
                for index in range(self.NUM_PLAYERS):
                    the_names[input(f'Enter a name for player #{index + 1}: ')] = False

            print(f'You entered the following names: {the_names}')

            while True:
                correct_names = input('\nIs this list correct (Y/N): ')

                if correct_names == 'y':
                    break
                elif correct_names == 'n':
                    the_names.clear()
                    break
                else:
                    print('\nPlease enter Y for yes or N for no')
        
        return the_names
    

    def initialize_players(self):
        self.get_number_of_players()
        players_names = self.get_players_names()
        
        for name, is_a_kid in players_names.items():
            self.players = Player(name, is_a_kid)
