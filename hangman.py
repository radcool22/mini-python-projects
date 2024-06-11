import random 

def main():
    words = ["class", "study", "learn", "teach", "books", "pupil", "exams", "notes", "grade", "chalk", "quiz", "paper", "desk", "tutor", "course"]
    chosen_word = random.choice(words)
    word_display = ["_" for _ in chosen_word]
    attempts = 10

    print("Welcome to Hangman!")

    while attempts > 0 and "_" in word_display:
        print("\n" + " ".join(word_display))
        guess = input("Guess a letter: ").lower()
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[index] = guess
        else:
            print("That letter is not in the word. Try again.")
            attempts -= 1

    if "_" not in word_display:
        print("You guessed the word!")
        print(" ".join(word_display))
        print("Well done!")
    else:
        print("You ran out of attempts! The word was " + chosen_word)
        print("You lost!")

if __name__ == "__main__":
    main()