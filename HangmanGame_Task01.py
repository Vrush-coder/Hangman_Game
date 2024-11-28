import random

# List of words for the game
word_list = ['python', 'programming', 'hangman', 'developer', 'engineering', 'machine', 'learning','apple','student','and']

def choose_word():
    #Select a random word from the list
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Display the word with guessed letters and underscores."""
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game():
    print("Welcome to the Hangman Game!")
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Maximum number of incorrect guesses allowed
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Guesses left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You've guessed the word:", word)
                break
        else:
            print("Wrong guess!")
            attempts -= 1
    
    if attempts == 0:
        print("\nYou've run out of attempts! The word was:", word)

if __name__ == "__main__":
    hangman_game()
