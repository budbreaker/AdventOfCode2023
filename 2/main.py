cubes_map = {
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    "red": 12,
    "green": 13,
    "blue": 14
}


def extract_id(linee):
    return linee.split(":")[0].split(" ")[1], linee.split(":")[1].split(";")


def invalid_game(games_arr):
    invalid = False
    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for game in games_arr:
        game = game.split(",")
        for cubes in game:
            cubes = cubes.strip()
            number = int(cubes.split(" ")[0])
            color = cubes.split(" ")[1]
            if number > cubes_map[color]:
                invalid = True
            if number > min_cubes[color]:
                min_cubes[color] = number
    return invalid, min_cubes


def multiply_cubes(map):
    return map["red"] * map["green"] * map["blue"]


with open("input.txt") as f:
    lines = f.readlines()
    possible_games = []
    summ = 0
    for line in lines:
        line.strip()
        game_id, games = extract_id(line)
        print(line)
        print("Id = " + game_id)
        print(games)
        is_invalid, minimum_cubes = invalid_game(games)
        print(minimum_cubes)
        summ += multiply_cubes(minimum_cubes)
        if is_invalid:
            print("Invalid game")
            continue
        print("Valid game")
        possible_games.append(int(game_id))

    print(sum(possible_games))
    print(summ)
