from DictionaryServices import DCSCopyTextDefinition as Define
from Class_Player import Player

SCORE_FOR_KIDS = False

def is_a_valid_word(search_word:str, len_word:int) -> bool:
        search_result = Define(None, search_word, (0, len_word))

        if search_result:
            return True
        else:
            return False


def set_score(a_player:Player) -> None: #list_of_words:list[str]
    score = 0
        
    for each_word in a_player.players_words.list_of_words:
        length_of_word = len(each_word)
            
        if is_a_valid_word(each_word, length_of_word):
        
            #if SCORE_FOR_KIDS and length_of_word == 2:
            if a_player.is_a_kid and length_of_word == 2:
                score += 1
            elif 3 <= length_of_word <= 4:
                score += 1
            elif length_of_word == 5:
                score += 2
            elif length_of_word == 6:
                score += 3
            elif length_of_word == 7:
                score += 5
            else:
                score += 11
        
    a_player.score = score

# Created but not currently used
#
#       see DISPLAY_FINAL_SCORES for use
#
def get_list_of_players_sorted_by_high_score(list_of_players):
    list_of_scores = [p.score for p in list_of_players]

    return sorted(list(enumerate(list_of_scores)), key=lambda x: x[1], reverse=True)


def display_final_scores(list_of_players):
    # Generate an enumerated list players sorted by score
    #
    #   (1) Generate a list of all players scores
    #   (2) Enumerate this list to retain the index of the player for a given score
    #   (3) Sort the enumerated list in reverse to obtain a high score list in descending order
    #
    # Each item players_sorted_high_to_low_score in is of the form:
    #
    #      (<index>, <players score>)
    #
    #       <index> is used to access the specific player for <player score>
    #
    # Yes this can be separated out into several lines
    players_sorted_high_to_low_score = sorted(list(enumerate([p.score for p in list_of_players])), key=lambda x: x[1], reverse=True)

    for player in players_sorted_high_to_low_score:
        print(f'\n{list_of_players[player[0]].name} has score = {player[1]}')


def list_display_final_scores(list_of_players):
    list_of_scores = [player.score for player in list_of_players]
    max_scores = max(list_of_scores)
    indices_of_max_scores = [index for index, score in enumerate(list_of_scores) if score == max_scores]

    if len(indices_of_max_scores) == 1:
        print(f'The winner is {list_of_players[indices_of_max_scores[0]].name} with a score of {list_of_players[indices_of_max_scores[0]].score}')
    elif len(indices_of_max_scores) == len(list_of_players):
        print('All players tied .... ')
    else:
        display_final_scores(list_of_players)


def dict_display_final_scores(list_of_players) -> None:
    dict_of_names_and_scores = {name:score for name,score in zip([p.name for p in list_of_players],[p.score for p in list_of_players])} 
    dict_sorted_by_high_score = dict(sorted(dict_of_names_and_scores.items(), key=lambda x: x[1], reverse=True))
    list_of_players_with_high_score = [name for name in dict_sorted_by_high_score if dict_sorted_by_high_score[name] == max(dict_sorted_by_high_score.values())]

    if len(list_of_players_with_high_score) == 1:
        print(f'The winner is {list_of_players_with_high_score[0]} with a score of {dict_of_names_and_scores[list_of_players_with_high_score[0]]}')
    elif len(list_of_players_with_high_score) == len(list_of_players):
        print('All players tied .... ')
    else:
        print(f'We have {len(list_of_players_with_high_score)} winners!!\n')
        print(f"{'Name' : <10}{'Score' : >10}")
        print('-'*20)
        for k, v in dict_sorted_by_high_score.items():
            print(f"{k : <10}{v : ^15}")



#####################################################################
# TEST
#
#   Open Class_Words and adjust END_TIME if necessary.
#   Use NUM_MINS = 1 / x for < 60 seconds
#####################################################################
""" from Class_Words import Words
from Class_Board import Board
w = Words()
b = Board()
b.print_board()
w.collect_words(b)
the_score = get_score(w.list_of_words)
print(the_score) """