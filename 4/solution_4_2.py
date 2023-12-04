from solution_4_1 import Game

class NewGame(Game):
    def __init__(self, string) -> None:
        super().__init__(string)
    
    def points(self):
        cnt = 0
        for nb in self.ownNbs:
            if nb in self.winningNbs:
                cnt +=1
        return cnt

if __name__ == "__main__":
    with open("input.txt") as input:
        games = [NewGame(line) for line in input]
        won_scratchcards = [1 for _ in range(len(games))]
        for idx, game in enumerate(games):
            if game.points():
                for i in range(idx+1,min(len(games), idx+game.points()+1)):
                    won_scratchcards[i] += won_scratchcards[idx]
        print(sum(won_scratchcards))

    # My first attempt was a queue implementatation that does technically work on small problems,
    # but because of how the number of cards scales like a factorial it becomes completely unworkable.
    with open("input.txt") as input:
        games = [NewGame(line) for line in input]
        copied_scratchcards = []
        for idx, game in enumerate(games):
            if game.points():
                copied_scratchcards.extend(games[idx+1:min(len(games), idx+game.points()+1)])
        # Very inneficient
        cnt = 0
        while copied_scratchcards:
            cnt += 1
            if cnt % 100000 == 0:
                print(f"Processed {cnt} cards.")
            game = copied_scratchcards.pop(0)
            copied_scratchcards.extend(games[game.cardIdx:min(len(games), game.cardIdx+game.points())])
        print(cnt+len(games))





        
