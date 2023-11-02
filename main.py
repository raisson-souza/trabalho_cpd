# fazer por igualdade e depois ir por intervalo
# nao vale build in
from datetime import datetime
from generate_random_games import generate_random_games

class Node:
    Game = None
    L = None # ESQUERDO
    R = None # DIREITO

    def __init__(self, game):
        self.Game = game
        self.L = None
        self.R = None

initial = datetime.now()
games = generate_random_games(100000)
final = datetime.now()
print(final - initial)
# input()
