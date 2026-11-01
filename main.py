import random


def guess_number():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))

            if 1 <= guess <= 100:
                return guess
            else:
                print("Choose a number between 1 and 100!")

        except ValueError:
            print("Please enter a valid number!")


def game():
    number = random.randint(1, 100)
    count = 0

    print("Guess a number between 1 and 100.")
    print("You have 10 attempts!")

    while True:
        guess = guess_number()
        count += 1

        if guess == number:
            print("Congratulations! You win! 😍")
            print("The number was:", number)
            print("Your attempts:", count)
            break

        elif count >= 10:
            print("Too many guesses! Game over!")
            print("The number was:", number)
            print("Your attempts:", count)
            break

        elif guess < number:
            print("Try a higher number!")

        else:
            print("Try a lower number!")


def main():
    play = "y"

    while play == "y":
        game()
        play = input("Do you wanna play again? (y/n): ").strip().lower()

main()
