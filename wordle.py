#Elizabeth Hooton
#eh151720@ohio.edu
#Section 100

# imports required for code to work
import csv
from random import randint
from termcolor import colored

class Guess:

    def __init__(self):
        # Attempted guess made by user
        self.guess_attempt = ' '*5
        # A list of integers for feedback on the guess  
        self.letter_state = [0]*5# 0: Not in word | 1: Incorrect position | 2: Correct position

# updates how each character in the user's guess is compared to the solution
    def update_guess(self, attempt, solution):
        '''This method will update the letter state for each letter in the guess'''
        count = {l : solution.count(l) for l in attempt}
        for i, l in enumerate(attempt):
            if l == solution[i]:
                self.letter_state[i] = 2
                count[l] -= 1

        for i, l in enumerate(attempt):
            if l in solution:
                if count [l] != 0:
                    if self.letter_state[i] == 0:
                        self.letter_state[i] = 1
                        count[l] -= 1


        self.guess_attempt=attempt

class Wordle:

# defines variables
    def __init__(self, num_attempts = 6):
        self.num_attempts = num_attempts
        self.current_attempt = 0
        self.guesses = [Guess() for i in range(num_attempts)]
        self.allowed = []
        self.answers = []
        self.solution = ""
        self.is_solved = False


# imports file and creates two lists of the content, also creates a random solution
    def load_words(self, filename):
        '''Opens the .csv file given by file_name, then load self.allowed and self.answers'''
        f = open(filename, 'r')
        csv_content = list(csv.reader(f, delimiter = ','))

        
        self.allowed = [ x[0] for x in csv_content ]
        
        self.answers = [x[1] for x in csv_content if x[1] != '']

        x = randint(0, len(self.answers))
        
        self.solution = self.answers[x]
        

# makes your own solution for testing
    def set_solution(self, solution):
        '''(For debug/testing) Manually sets the self.solution'''
        self.solution = solution


# prints out the current guesses and states so far   
    def print_board(self):
        '''Displays the current state of all guesses so far'''
        for guess in self.guesses:
            for i in range(5):
                if guess.letter_state[i] == 0:

                    if i == 4:
                        x = colored(guess.guess_attempt[i],'white', 'on_grey')
                        print(x, end='')
                        
                    else:
                        y = colored(f'{guess.guess_attempt[i]}','white', 'on_grey')
                        print(y, end='|')
                        
                if guess.letter_state[i] == 1:

                    if i == 4:
                        x = colored(guess.guess_attempt[i],'white', 'on_yellow')
                        print(x, end='')
                        
                    else:
                        y = colored(f'{guess.guess_attempt[i]}','white', 'on_yellow')
                        print(y, end='|')
                
                if guess.letter_state[i] == 2:

                    if i == 4:
                        x = colored(guess.guess_attempt[i],'white', 'on_green')
                        print(x, end='')
                        
                    else:
                        y = colored(f'{guess.guess_attempt[i]}','white', 'on_green')
                        print(y, end='|')
            print ('')

            

# determines if the guess from the user is valid, updates the attempts, and determines if the wordle is solved
    def make_guess(self, attempt):
        '''Inputs a guess from the user, then updates the current guess.letter_state'''

        while attempt not in self.allowed or len(attempt)!=5:
            if attempt not in self.allowed:
                print('Attempt not allowed!')
            elif len(attempt)!=5:
                print('Guess should be 5 characters!')
            attempt = input('Enter a new guess!:\n').lower()


        self.guesses[self.current_attempt].update_guess(attempt, self.solution)
        self.current_attempt+=1
        
        if attempt == self.solution:
            self.is_solved = True   
            

if __name__ == "__main__":



    z = colored('''


.--.      .--.    ,-----.    .-------.     ______       .---.       .-''-.   
|  |_     |  |  .'  .-,  '.  |  _ _   \   |    _ `''.   | ,_|     .'_ _   \  
| _( )_   |  | / ,-.|  \ _ \ | ( ' )  |   | _ | ) _  \,-./  )    / ( ` )   ' 
|(_ o _)  |  |;  \  '_ /  | :|(_ o _) /   |( ''_'  ) |\  '_ '`) . (_ o _)  | 
| (_,_) \ |  ||  _`,/ \ _/  || (_,_).' __ | . (_) `. | > (_)  ) |  (_,_)___| 
|  |/    \|  |: (  '\_/ \   ;|  |\ \  |  ||(_    ._) '(  .  .-' '  \   .---. 
|  '  /\  `  | \ `"/  \  ) / |  | \ `'   /|  (_.\.' /  `-'`-'|___\  `-'    / 
|    /  \    |  '. \_/``".'  |  |  \    / |       .'    |        \\       /  
`---'    `---`    '-----'    ''-'   `'-'  '-----'`      `--------` `'-..-'   
                   ''', 'red')

    print (z)

                   
# runs the game by calling the make_guess and print_board functions, prints messages to the user based on the state of their attempt
    game = Wordle()
    game.load_words('word_data.csv')
    for i in range(game.num_attempts):

        g = input('Enter a new guess!:\n').lower()
        game.make_guess(g)
        game.print_board()

        if game.is_solved:
            print('Congratulations, you solved the wordle! (:')
            break

    if not game.is_solved:
        print(f'You lost ): The solution to the wordle is {game.solution}!')
