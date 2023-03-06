import random

class Hangman:

    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = random.choice(self.possible_words)
        self.lives = 5
        self.correctly_guessed_letters = list('_' * len(self.word_to_find))
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        letter = str(input('Enter a letter'))
        if len(letter) == 1 and letter.isalpha():
            if letter in self.word_to_find:
                self.turn_count += 1
                print('That letter is in the word')
                for index, char in enumerate(self.word_to_find):
                    if char == letter:
                        self.correctly_guessed_letters[index] = letter
            else:
                self.turn_count += 1
                self.error_count += 1
                self.lives -= 1
                print('That letter is not in the word')
        else:
            print('Please enter a letter')


    def start_game(self):
        while self.lives > 0 :
            print(''.join(self.correctly_guessed_letters))
            print('Wrong letter'.join(self.wrongly_guessed_letters))
            print('Lives left:', self.lives)
            print('Error count:', self.error_count)
            print('Turn count:', self.turn_count)
            self.play()
            if self.lives == 0:
                self.game_over()
            elif '_' not in self.correctly_guessed_letters:
                self.well_played()
                break          
    
            
    def game_over(self):
        print('Game over...')

    def well_played(self):
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")
  
    

Hangman().start_game()

