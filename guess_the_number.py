import random
number = random.randint(1, 10)

# Testing VSC git commits
def main():
    while True:
        user_input = int(input("Choose a number between 1 and 10: "))

        if user_input > number:
            print("Your guess is higher than the number. Try again.")
        elif user_input < number:
            print("Your guess is lower than the number. Try again.")
        elif user_input == number:
            print("Congratulations! You guessed the number!")
            break
        else:
            print("Sorry, that's an invalid format. Try again later.")
            break

if __name__ == "__main__":
    main()
