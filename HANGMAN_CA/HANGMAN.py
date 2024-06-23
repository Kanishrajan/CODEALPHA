import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'blueberry', 'melon']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()

def display_hangman(attempts):
    hangman_display = [
        "  ____\n |    |\n      |\n      |\n      |\n______|",
        "  ____\n |    |\n O    |\n      |\n      |\n______|",
        "  ____\n |    |\n O    |\n |    |\n      |\n______|",
        "  ____\n |    |\n O    |\n/|    |\n      |\n______|",
        "  ____\n |    |\n O    |\n/|\\   |\n      |\n______|",
        "  ____\n |    |\n O    |\n/|\\   |\n/     |\n______|",
        "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n______|"
    ]
    return hangman_display[attempts]

def hangman():
    max_attempts = 6
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))
    print(display_hangman(attempts))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts += 1

        print(display_word(word_to_guess, guessed_letters))
        print(display_hangman(attempts))

        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        if attempts >= max_attempts:
            print("You ran out of attempts! The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
