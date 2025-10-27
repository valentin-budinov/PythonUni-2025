import random

def play_game():
    secret_number = random.randint(1, 10)

    player_guess = None
    guesses = 0

    while player_guess != secret_number:
        player_guess = int(input("Guess a number between 1 and 10: "))

        if player_guess <= 0 or player_guess > 10:
            print("The number must be between 1 and 10. Try again.")
        elif player_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        guesses += 1

    print(f"Congratulations! You guessed that the secret number was {secret_number} with {guesses} guesses!.")

while True:
    play_game()
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()

    if play_again == "no":
        print("Thanks for playing! Goodbye!")
        break
