from random import randint

class Game:
    Id : int
    Title : str
    Developer : str
    Price : float
    Genres : list

    def __init__(self, id, title, developer, price, genres):
        self.Id = id
        self.Title = title
        self.Developer = developer
        self.Price = price
        self.Genres = genres

def generate_random_games(quantity : int):
    titles01 = ["A Aventura de ", "A Lenda de ", "A Caça de ", "A ", "O ", "A Morte de "]
    titles02 = ["Dora", "Ethan", "Mortis", "Lukia", "Ross", "Cuic"]
    titles_l = len(titles01) - 1
    developers = ["CuiCodeSystems", "AMF Softwares", "Tech", "OntoSystems"]
    genres = ["RPG", "Action", "Strategy"]

    games = []
    for i in range(quantity):
        title = titles01[randint(0, titles_l)] + titles02[randint(0, titles_l)]
        developer = developers[randint(0, len(developers) - 1)]
        price = randint(0, 500)
        genre = genres[randint(0, len(genres) - 1)]
        games.append(Game(i, title, developer, price, genre))
    return games
