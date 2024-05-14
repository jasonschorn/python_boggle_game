from Class_Words import Words


########################################################################################
# CLASS_
########################################################################################
class Player:

    def __init__(self, name:str, is_a_kid:bool) -> None:
        self.name = name
        self.players_words = Words()
        self.score = 0
        self.is_a_kid = is_a_kid
    

    def set_score(self) -> None:
        self.score = self.players_words.get_score()

    def reset_player(self) -> None:
        self.score = 0
        self.players_words.reset_list_of_words()

###################################################################
# TEST --> TEST PLAYER
###################################################################
""" from Class_Board import Board
b = Board()
b.print_board()
p = Player('Jason')
p.players_words.collect_words(b)
print(p.players_words.list_of_words)
p.set_score()
print(p.score) """

'''from random import randint

def get_players_sorted_by_high_score(list_of_players):
    list_of_scores = [p.score for p in list_of_players]

    return sorted(list(enumerate(list_of_scores)), key=lambda x: x[1], reverse=True)


p1 = Player('Jason')
p2 = Player('Teresa')
p3 = Player('Savoy')
p4 = Player('Larisa')
p5 = Player('Maxwell')
p6 = Player('Phoenix')
players = [p1,p2,p3,p4,p5,p6]
for p in players:
    p.score = randint(2,10)

list_of_scores = [p.score for p in players]
max_scores = max(list_of_scores)
index_max_scores = [index for index, score in enumerate(list_of_scores) if score == max_scores]

print(list_of_scores)

for item in get_players_sorted_by_high_score(players):
    print(f'{players[item[0]].name} has score = {item[1]}')


print(f'Number of max scores = {len(index_max_scores)} with indices = {index_max_scores}')

for index in index_max_scores:
    print(f'{players[index].name} has a high score = {players[index].score}')

name_p = [p.name for p in players]
score_p = [p.score for p in players]

ab = {a:b for a,b in zip([p.name for p in players],[p.score for p in players])} 
print(ab)

d = {a:b for a,b in zip(name_p,score_p)}
ds = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
#max_d = max(d.values())
max_p = [key for key in d if d[key]== max(d.values())]

if len(max_p) == 1:
    print(f'The winner is {max_p[0]} with a score of {d[max_p[0]]}')
elif len(max_p) == len(d):
    print('All players tied...no winner!')
else:
    print(f'We have {len(max_p)} winners:')
    for player in max_p:
        print(f'\t{player}')

print(f"{'Name' : <10}{'Score' : >10}")
print('-'*20)
for k, v in ds.items():
    print(f"{k : <10}{v : ^15}")
            
        

p1.score = 4
p2.score = 4
p3.score = 3

pscores = [ps.score for ps in lp]
mscore = max(pscores)
more_than_one_max = [index for index, value in enumerate(pscores) if value == mscore]
 '''


