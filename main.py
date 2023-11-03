from datetime import datetime
import generate_random_games

def generate_games(quantity : int):
    """Geração de jogos aleatórios"""
    initial = datetime.now()
    games = generate_random_games.generate_random_games(quantity)
    final = datetime.now()
    print(f"Tempo de geração de { quantity } jogos: { final - initial }")
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
    """Printa as principais informações dos jogos"""
    if root is None:
        return
    print_bst(root.L)
    print(f"Jogo: { root.Game.Title } | Categoria: { root.Game.Genres } | Preço: R${ root.Game.Price }")
    print_bst(root.R)

def generate_price_bst(games : list):
    """Gera a BST ordenada por preço"""

    def insert_price_bst(root : Node, game : generate_random_games.Game):
        """Função de inserção de jogos na BST ordenada por preço"""
        if root == None:
            return Node(game)
        elif game.Price > root.Game.Price:
            root.L = insert_price_bst(root.L, game)
        else:
            root.R = insert_price_bst(root.R, game)
        return root

    initial = datetime.now()
    bst = None
    for game in games:
        bst = insert_price_bst(bst, game)
    final = datetime.now()
    print(f"Tempo de geração da BST ordenada por preço: { final - initial }")

    return bst

def search_games_by_price(bst : Node, price : int):
    """Procura jogos na BST ordenada por preço por preço exato"""
    initial = datetime.now()
    games_found = []

    def search(node : Node):
        if node is None:
            return

        if node.Game.Price == price:
            games_found.append(node.Game)

        search(node.L)
        search(node.R)

    search(bst)
    final = datetime.now()
    print(f"Tempo de busca de jogos por preço fixo R$ { price }: { final - initial }")
    return games_found

def search_games_by_price_range(bst : Node, min_price : int, max_price : int):
    """Procura jogos na BST ordenada por preço por intervalo de preço"""
    initial = datetime.now()
    games_found = []

    def search(node : Node):
        if node is None:
            return

        if node.Game.Price > min_price and node.Game.Price < max_price:
            games_found.append(node.Game)

        search(node.L)
        search(node.R)

    search(bst)
    final = datetime.now()
    print(f"Tempo de busca de jogos por intervalo de preço (R${ min_price } - R${ max_price }): { final - initial }")
    return games_found

games = generate_games(150000)

bst = generate_price_bst(games)
# print_bst(bst)

found_games_100 = search_games_by_price(bst, 100)
found_games_200 = search_games_by_price(bst, 200)
found_games_300 = search_games_by_price(bst, 300)

found_games_range_100_150 = search_games_by_price_range(bst, 100, 150)
found_games_range_0_50 = search_games_by_price_range(bst, 0, 50)

input()
