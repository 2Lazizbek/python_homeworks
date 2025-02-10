import random
user_response = "yes"
yes = ['Y', 'YES', 'y', 'yes', 'ok']
while user_response in yes:
    number = random.randint(1, 100)
    print("Number between 1 and 100 selected.")
    for i in range(10):
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You guessed it right!")
            user_response = "no"
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
    else:
        user_response = input("You lost. Want to play again? ")