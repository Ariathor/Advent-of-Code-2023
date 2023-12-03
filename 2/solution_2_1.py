class Draw():
    def __init__(self, string) -> None:
        draw = string.strip()
        colors = draw.split(",")
        self.red = 0
        self.blue = 0
        self.green = 0
        for entry in colors:
            entry = entry.strip()
            number, color = entry.split()
            match color.strip():
                case "red":
                    self.red = int(number.strip())
                case "green":
                    self.green = int(number.strip())
                case "blue":
                    self.blue = int(number.strip())

class Game():
    def __init__(self, string):
        self.draw = None
        game, sets = string.strip().split(":")
        self.gameIdx = int(game.replace("Game ", ""))  # Could have just kept row number considering the input file is ordered
        # Could just iterate through the line and find the max value for each color, but I have a hunch parsing it will make the second question easier
        subsets = sets.split(";")
        self.draws = set()
        for subset in subsets:
            self.draws.add(Draw(subset))

if __name__ == "__main__":
    MAXRED = 12
    MAXGREEN = 13
    MAXBLUE = 14

    with open("input.txt") as input:
        idxSum = 0
        for line in input:
            my_game = Game(line)
            game_possible = True
            for draw in my_game.draws:
                if draw.red > MAXRED or draw.green > MAXGREEN or draw.blue > MAXBLUE:
                    game_possible = False
                    break;
            if game_possible:
                idxSum += my_game.gameIdx
        print(idxSum)