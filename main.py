import random

class WordScramble:
    def __init__(self):
        self.words = [
            "python", "programming", "algorithm", "computer", "code",
            "challenge", "word", "puzzle", "game", "learning"
        ]
        self.secret_word = random.choice(self.words)
        self.scrambled_word = self.scramble_word(self.secret_word)
    
    def scramble_word(self, word):
        scrambled = list(word)
        random.shuffle(scrambled)
        return ''.join(scrambled)
    
    def play_game(self):
        print("Welcome to Word Scramble!")
        print(f"Unscramble the word: {self.scrambled_word}")

        attempts = 3
        while attempts > 0:
            guess = input("Your guess: ").strip().lower()

            if guess == self.secret_word:
                print("Congratulations! You've guessed the word correctly.")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect guess. Try again. You have {attempts} attempts left.")
                else:
                    print(f"Sorry, you've run out of attempts. The word was '{self.secret_word}'.")

if __name__ == "__main__":
    game = WordScramble()
    game.play_game()
