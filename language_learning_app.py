import random

def main():
    words = [
        {"Spanish": "hola", "English": "hello"},
        {"Spanish": "adios", "English": "goodbye"},
        {"Spanish": "por favor", "English": "please"},
        {"Spanish": "gracias", "English": "thank you"},
        {"Spanish": "si", "English": "yes"},
        {"Spanish": "no", "English": "no"},
        {"Spanish": "lo siento", "English": "sorry"},
        {"Spanish": "buenos dias", "English": "good morning"},
        {"Spanish": "buenas noches", "English": "good night"},
        {"Spanish": "como estas", "English": "how are you"},
        {"Spanish": "bien", "English": "good"},
        {"Spanish": "mal", "English": "bad"},
        {"Spanish": "amigo", "English": "friend"},
        {"Spanish": "familia", "English": "family"},
        {"Spanish": "comida", "English": "food"}
    ]

    def quiz_user(words)    :
        random.shuffle(words)
        score = 0

        for word in words:
            print("What is the english translation of " + word['Spanish'] + "?")
            user_answer = input("Your answer: ").strip().lower()
            correct_answer = word["English"].lower()

            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is " + word["English"] + ".")

        print("Quiz complete! Your score is " + str(score))

    print("Welcome to the Spanish Learning App!")
    input("Press enter to start the quiz ")
    quiz_user(words)

if __name__ == "__main__":
    main()