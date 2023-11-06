from datetime import datetime
import generate_random_games
import sys

sys.setrecursionlimit(500001)

def generate_games(quantity : int):
    """Geração de jogos aleatórios"""
    initial = datetime.now()
    games = generate_random_games.generate_random_games(quantity)
    final = datetime.now()
    print(f"Tempo de geração de { quantity } jogos: { final - initial }")
    return games

def get_mocked_games():
    """Captura de jogos pré-gerados e estáticos"""
    initial = datetime.now()
    file = open("mocked_games.txt", "r")
    lines = file.readlines()
    lines_len = len(lines)

    def treat_genre_line(genre_line : str) -> list:
        return genre_line.replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(",")

    games = []
    for line in lines:
        line = line.replace("\n", "")
        game_info = line.split("#")
        game_genres = treat_genre_line(game_info[4])
        games.append(generate_random_games.Game(
            int(game_info[0]),
            game_info[1],
            game_info[2],
            int(game_info[3]),
            game_genres
        ))

    final = datetime.now()
    print(f"Tempo de leitura de { lines_len } jogos: { final - initial }")

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
        elif node.Game.Price == price:
            games_found.append(node.Game)
            search(node.R)
        elif node.Game.Price < price:
            search(node.L)
        else:
            search(node.R)

    search(bst)
    # search(bst.L if bst.Game.Price < price else bst.R)
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

def encrypt_genre(genre_name : str):
        return genre_name.lower()

def generate_genres_obj(games : list):
    """Gera um objeto com gêneros em hash"""
    genres_list = {}

    def insert_genres_obj(game : generate_random_games.Game):
        """Função de inserção de jogos no objeto com gêneros em hash"""
        for genre in game.Genres:
            encrypted_genre = encrypt_genre(genre)
            if encrypted_genre in genres_list:
                genres_list[encrypted_genre].append(game)
            else:
                genres_list[encrypted_genre] = [game]

    initial = datetime.now()
    for game in games:
        insert_genres_obj(game)
    final = datetime.now()
    print(f"Tempo de geração do objeto com gêneros: { final - initial }")
    return genres_list

def search_game_by_genre(genres_json, genre : str):
    initial = datetime.now()
    games_found = []
    encrypted_genre = encrypt_genre(genre)

    if encrypted_genre in genres_json:
        games_found = genres_json[encrypted_genre]

    final = datetime.now()
    print(f"Tempo de busca de jogos do gênero { genre }: { final - initial }")
    return games_found

# games = generate_games(200000)
games = get_mocked_games()

bst = generate_price_bst(games)
# print_bst(bst)

found_games_100 = search_games_by_price(bst, 100)
found_games_200 = search_games_by_price(bst, 200)
found_games_300 = search_games_by_price(bst, 300)

found_games_range_100_150 = search_games_by_price_range(bst, 100, 150)
found_games_range_0_50 = search_games_by_price_range(bst, 0, 50)

genres_list = generate_genres_obj(games)

action_games = search_game_by_genre(genres_list, "Action")
strategy_games = search_game_by_genre(genres_list, "Strategy")
rpg_games = search_game_by_genre(genres_list, "rpg")
terror_games = search_game_by_genre(genres_list, "terror")

input()
