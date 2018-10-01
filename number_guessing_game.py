import random

def guess_the_number():
    game = True
    # Choose a random integer between 0 and 99 inclusive
    correct_guess = random.randint(0, 100)
    guess = input("Enter your guess (whole numbers only) 🐢 ->")
    int_guess = int(guess)

    while game == True:

        if int_guess < correct_guess:
            print("Your guess was too LOW!")
            guess = input("Enter your NEW guess (whole numbers only) 🐢 ->")
            int_guess = int(guess)
        elif int_guess > correct_guess:
            print("Your guess was too HIGH!")
            guess = input("Enter your NEW guess (whole numbers only) 🐢 ->")
            int_guess = int(guess)
        else:
            print("Congratulations! You guessed correctly! 🎉🎉🎉")
            game = False

guess_the_number()