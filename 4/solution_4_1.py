class Game():
    def __init__(self, string) -> None:
        self.cardIdx = None
        self.winningNbs = set()
        self.ownNbs = list()
        self.string = string

        self.cardIdx = int(string.split(":")[0].replace("Card ", ""))
        self.winningNbs = {int(nb) for nb in string.split("|")[0].split(":")[1].split()}
        self.ownNbs = [int(nb) for nb in string.split("|")[1].split()]
    
    # Calculate how many own numbers are in own numbers, then convert to equivalent reward points
    def points(self):
        cnt = 0
        for nb in self.ownNbs:
            if nb in self.winningNbs:
                cnt +=1
        return 2**(cnt-1) if cnt > 0 else 0
    
    def __repr__(self) -> str:
        return self.string
    
if __name__ == "__main__":
    with open("input.txt") as input:
        sum = 0
        for line in input:
            game = Game(line)
            sum += game.points()
        print(sum)
