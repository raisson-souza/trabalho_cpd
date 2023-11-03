from generate_random_games import generate_random_games

def generate_games(quantity : int):
    games = generate_random_games(quantity)

    file = open("mocked_games.txt", "w")

    for game in games:
        file.write(f"{ game.Id }#{ game.Title }#{ game.Developer }#{ game.Price }#{ game.Genres }\n")

generate_games(500000)
