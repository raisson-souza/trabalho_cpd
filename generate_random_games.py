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

def generate_genre(genres_list):
    genres = []
    c = randint(1, 3)

    while c != 0:
            chosen_genre = genres_list[randint(0, len(genres_list) - 1)]
            try:
                if genres.index(chosen_genre) != None:
                    pass
            except:
                genres.append(chosen_genre)
                c -= 1

    return genres

def generate_random_games(quantity : int):
    titles01 = ["A Aventura de ", "A Lenda de ", "A Caça de ", "A ", "O ", "A Morte de ", "O Show de "]
    titles02 = ["Dora", "Ethan", "Mortis", "Lukia", "Ross", "Cuic", "Alex"]
    titles_l = len(titles01) - 1
    developers = ["CuiCodeSystems", "AMF Softwares", "Tech", "OntoSystems"]
    genres_list = ["RPG", "Action", "Strategy", "Adventure", "Simulation", "Sports"]

    games = []
    for i in range(quantity):
        title = titles01[randint(0, titles_l)] + titles02[randint(0, titles_l)]
        developer = developers[randint(0, len(developers) - 1)]
        price = randint(0, 500)
        genres = generate_genre(genres_list)
        games.append(Game(i, title, developer, price, genres))
    return games
