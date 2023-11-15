from datetime import datetime
from generate_random_games import generate_random_games

def generate_games(quantity : int):
    initial = datetime.now()
    games = generate_random_games(quantity)
    final = datetime.now()
    print(f"Tempo de geração de { quantity } jogos: { final - initial }")

    file = open(f"mocked_games_{ quantity }.txt", "w")

    for game in games:
        file.write(f"{ game.Id }#{ game.Title }#{ game.Developer }#{ game.Price }#{ game.Genres }\n")

    file.close()

generate_games(10000)
generate_games(5000)
generate_games(2500)
generate_games(1000)
generate_games(500)
