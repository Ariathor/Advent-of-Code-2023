from solution_2_1 import Game

with open("input.txt") as input:
    sumPowerSets = 0
    for line in input:
        minRed = 0
        minBlue = 0
        minGreen = 0
        my_game = Game(line)
        for draw in my_game.draws:
            if draw.red > minRed:
                minRed = draw.red
            if draw.green > minGreen:
                minGreen = draw.green
            if draw.blue > minBlue:
                minBlue = draw.blue
        sumPowerSets += minBlue * minGreen * minRed
        
    print(sumPowerSets)