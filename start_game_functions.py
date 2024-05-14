import subprocess
import datetime


def get_end_time():
    return datetime.datetime.now() + datetime.timedelta(minutes=get_length_of_game_timer())


def start_or_end_game() -> bool:
    print('\nStart a game [Y = Yes or N = No]')

    while True:
        choice = input('Enter your choice: ').lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Please enter either Y or N')



def set_game_scoring_for_kids() -> bool:
    print()
    print('='*70)
    print('Play game with Normal or Kids scoring')
    print('\nOptions: \n\tKids Scoring = K \n\tNormal Scoring = N')
    print('='*70)

    while True:
        choice = input('\nEnter your choice: ').lower()

        if choice == 'k':
            return True
        elif choice == 'n':
            return False
        else:
            print('Please enter either N or K')


def get_length_of_game_timer() -> int:
    print()
    print('='*70)
    print("Set timer for how long a player gets to find words")
    print('\tEnter an integer value between 1 and 5')
    print('\tStandard play = 3 minutes')
    print('='*70)

    while True:
        try:
            
            choice = int(input('\nEnter your choice: '))
        except ValueError:
            print('Non-integer input given. Please try again...')
        else:
            if 1 <= choice <= 5:
                return choice


def get_number_of_rounds_per_game() -> int:
    print()
    print('='*70)
    print('Enter the number of rounds you would like to play')
    print('Enter an integer between 1 and 10')
    print('='*70)

    while True:
        try:
            
            choice = int(input('\nEnter your choice: '))
        except ValueError:
            print('Non-integer input given. Please try again...')
        else:
            if 1 <= choice <= 10:
                return choice

def get_game_type() -> str:
    game_types = ['Classic 4X4', 'New 4x4', 'Original 5x5', 
                  'Challenge 5x5', 'Deluxe 5x5', 'New 2012 5x5', 
                  'Super 6x6']
    
    print('Choose the type of Boggle game you would like to play: ')

    for num, val in enumerate(game_types):
        print(f'\t({num}) = {val}')
    
    while True:
        try:
            choice = int(input('\nPlease enter a choice [0 - 6]: '))
        except ValueError:
            print('Please enter an integer value')
        else:
            if 0 <= choice <= 6:
                return game_types[choice]
            else:
                print('Please enter a value between 0 and 6')


def display_instructions():
    subprocess.call(['open', '-a', 'Preview', '/Users/jasonschorn/Documents/Python/Code Files/Boggle/boggle_instructions.pdf'])


def gather_game_requirements():
    print()
    print('='*70)
    print('Prior to starting a game we need to gather some information\n')
    print(' '*10 + '(1) Which version of Boggle you would like to play')
    print(' '*10 + '(2) Whether to score the game for kids playing')
    print(' '*10 + '(3) Set the length  of time each player gets to find words')
    print(' '*10 + '(4) Set the number of rounds per game')
    print('='*70)

    while True:
        try:
            choice = input('\nPress R to read game instructions or B to begin gathering info: ').lower()
        except ValueError:
            print('Incorrect input type')
        else:
            if choice == 'b':
                return get_game_type(), set_game_scoring_for_kids(), get_length_of_game_timer(), get_number_of_rounds_per_game()            

        display_instructions()


