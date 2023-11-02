# fazer por igualdade e depois ir por intervalo
# nao vale build in
from datetime import datetime
import generate_random_games

def generate_games():
    initial = datetime.now()
    games = generate_random_games.generate_random_games(1000)
    final = datetime.now()
    print(final - initial)
    return games

class Node:
    Game = generate_random_games.Game
    L = None # ESQUERDO
    R = None # DIREITO

    def __init__(self, game : generate_random_games.Game):
        self.Game = game
        self.L = None
        self.R = None

def print_bst(root : Node):
    if root is None:
        return
    print_bst(root.L)
    print(f"Jogo: { root.Game.Title } | Preço: { root.Game.Price }")
    print_bst(root.R)

def insert_price_bst(root : Node, game : generate_random_games.Game):
    if root == None:
        return Node(game)
    elif game.Price > root.Game.Price:
        root.L = insert_price_bst(root.L, game)
    else:
        root.R = insert_price_bst(root.R, game)
    return root

def generate_price_bst(games : list):
    bst = None
    for game in games:
        bst = insert_price_bst(bst, game)
    return bst

games = generate_games()
bst = generate_price_bst(games)
print_bst(bst)

input()
