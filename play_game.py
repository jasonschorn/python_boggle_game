import datetime
from Class_Initialize_Players import Initialize_Players
from Class_Board import Board
from Class_Dice import Dice
import start_game_functions
import score_functions



def get_end_time(len_of_timer):
    return datetime.datetime.now() + datetime.timedelta(minutes=len_of_timer)


def play_boggle():
   
    while start_game_functions.start_or_end_game():
        game_type, set_scoring_for_kids, length_of_timer, num_rounds_per_game = start_game_functions.gather_game_requirements()
        the_players = Initialize_Players(set_scoring_for_kids)
        the_players.initialize_players()

        while num_rounds_per_game > 0:
            the_dice = Dice(game_type)
            the_board = Board(the_dice)

            for a_player in the_players.players:
                the_board.print_board()
                a_player.players_words.collect_words(the_board, get_end_time(length_of_timer))
                score_functions.set_score(a_player)

            score_functions.display_final_scores(the_players.players)

            num_rounds_per_game -= 1
            for a_player in the_players.players:
                a_player.reset_player()

