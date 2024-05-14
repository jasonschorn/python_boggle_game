import platform
from os import system
from play_game import play_boggle


def main():
    if platform.system == 'Windows':
        system('cls')
    else:
        system('clear')

    play_boggle()    
   

if __name__ == '__main__':

    main()

