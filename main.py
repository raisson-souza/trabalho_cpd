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

def search_games_by_price(bst : Node, price : int):
    games_found = []

    def search(node : Node):
        if node is None:
            return

        if node.Game.Price == price:
            games_found.append(node.Game)

        search(node.L)
        search(node.R)

    search(bst)
    return games_found

def search_games_by_price_range(bst : Node, min_price : int, max_price : int):
    games_found = []

    def search(node : Node):
        if node is None:
            return

        if node.Game.Price > min_price and node.Game.Price < max_price:
            games_found.append(node.Game)

        search(node.L)
        search(node.R)

    search(bst)
    return games_found

games = generate_games()
bst = generate_price_bst(games)
print_bst(bst)

found_games_100 = search_games_by_price(bst, 100)
found_games_200 = search_games_by_price(bst, 200)
found_games_300 = search_games_by_price(bst, 300)

found_games_range_100_150 = search_games_by_price_range(bst, 100, 150)
found_games_range_0_50 = search_games_by_price_range(bst, 0, 50)

input()
