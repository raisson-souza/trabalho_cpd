# fazer por igualdade e depois ir por intervalo
# nao vale build in
from random import randint

class Game:
    Id : int
    Title : str
    Developer : str
    Price : float
    Category : list

    def __init__(self, id, title, developer, price, category):
        self.Id = id
        self.Title = title
        self.Developer = developer
        self.Price = price
        self.Category

    def random_game():
        titles01 = ["A Aventura de ", "A Lenda de ", "A Caça de ", "A ", "O "]
        titles02 = ["Turabão", ""]

class Node:
    Game : Game
    L = None # ESQUERDO
    R = None # DIREITO

    def __init__(self, game):
        self.Game = game
        self.L = None
        self.R = None

jogo = Game(1, "titulo", "dev", 0, [])

game = Node(jogo)
game.L = Node(jogo)
game.R = Node(jogo)
