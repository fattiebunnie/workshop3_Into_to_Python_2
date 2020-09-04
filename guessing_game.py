import random
PLY_WIN = 6
PLY_CLOSE_GUESS = 1
COMP_CLOSE_GUESS = 1
COMP_WIN = 2
ANY_LOSE = 0

class Game:
    game_scores = {'Computer':[], 'Player':[]}
    round_scores = []
    comp = None
    ply = None

    def __init__(self):
        self.comp = Computer()
        self.ply = Player()
    
    def play_game(self):
        for i in range(5):
            self.play_round()
        comp_final_score = sum(self.game_scores['Computer'])
        ply_final_score = sum(self.game_scores['Player'])
        
        print("Computer final score: ", comp_final_score)
        print("Player final score: ", ply_final_score)
        if ply_final_score > comp_final_score:
            #note: \n means print an empty line in between this and the previous line
            print("\nYou won!")
        else:
            print("Sorry, the computer won, better luck next time!\n")

    def calc_round_scores(self):
        if self.ply.guess == self.comp.choice:
            print("You guessed it! You win 6 points, computer wins 0.\n")
            return [PLY_WIN, ANY_LOSE]
        # people to fill out themselves
        elif abs(self.ply.guess - self.comp.choice) == 1:
            print("Close guess! You win 1 point, computer wins 1.\n")
            return [PLY_CLOSE_GUESS, COMP_WIN]
        else: 
            print("Wrong guess! You win 0 points, computer wins 0.\n")
            return [ANY_LOSE, COMP_WIN]

    def play_round(self):
        # computer chooses a random number between 1 and 5
        self.comp.comp_choice()
        # player guesses a number between 1 and 5
        self.ply.player_guess()
        # show player which number the computer chose
        self.comp.print_comp_score()
        # determine player and computer scores 
        round_scores = self.calc_round_scores()
        self.game_scores['Computer'].append(round_scores[0])
        self.game_scores['Player'].append(round_scores[1])

class Player:
    def __init__(self):
        name = input("Hello, what is your name? ")
        self.name = name
        self.guess = 0
        print("Welcome," + self.name)

    def player_choice(self, guess):
        self.guess = guess

    def player_guess(self):
        self.guess = int(input("Please guess which number the computer is thinking of: "))

class Computer: 
    choice = 0
    def __init_(self):
        print("Let's play the guessing game! See if you can beat me!")

    def comp_choice(self):
        print("Computer has chosen a number between 1 and 5. ")
        self.choice = random.randint(1, 5)

    def print_comp_score(self):
        print("Computer chose: ", self.choice)

if __name__ == "__main__":
    game1 = Game()
    game1.play_game()
