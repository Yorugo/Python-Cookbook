import random

print("Welcome to the guessing game!")

# Computer generates a random number between 1 and 10
correct_answer = random.randint(1, 10)

# User has 3 guesses before losing the game
for count in range(3):
    # User guesses the number
    guess = int(input("Input your guess: "))

    # Computer tells user whether guess was too high or too low
    if guess < correct_answer:
        print("Your guess was too low.")
    elif guess > correct_answer:
        print("Your guess was too high.")
    else:
        print("Congratulations, you win!")
        break

    if 2-count == 1:
        print(f"You have {2 - count} guess remaining!\n")
    else:
        print(f"You have {2-count} guesses remaining!\n")
else:
    print(f"Sorry, you lose. The correct answer was: {correct_answer}.")
