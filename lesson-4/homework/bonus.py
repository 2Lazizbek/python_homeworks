import random
play_again = "yes"
score_computer = 0
score_user = 0
choices = {"p": "paper", "r": "rock", "s": "scissors"}
print("\n\n"+"#"*10, "Welcome to Rock-Paper-Scissors Game", "#"*10)
print("#"*10,"The first player to reach 5 points wins the game.","#"*10, "\n\n")
while score_user < 5 and score_computer < 5 and play_again == "yes":
    computer = random.choice(["p", "r", "s"])
    print("\nComputer has made its choice.")
    print('If you want to, enter "q" to quit the game.')
    user = input('Enter your choice["p" - paper, "r" - rock, "s" - scissors]: ')
    if user.lower() == "q":
        break
    while user.lower() not in ["p", "r", "s"]:
        print("Invalid choice. Please try again.")
        user = input('Enter your choice["p" - paper, "r" - rock, "s" - scissors]: ')
    user = user.lower()
    print(f"Computer: {choices[computer]}")
    print(f"User: {choices[user]}")
    if computer == user:
        print("Tie!")
    elif computer == "r" and user == "s":
        print("Computer wins!")
        score_computer += 1
    elif computer == "p" and user == "r":
        print("Computer wins!")
        score_computer += 1
    elif computer == "s" and user == "p":
        print("Computer wins! 1 point for computer!")
        score_computer += 1
    else:
        print("User wins! 1 point for user!")
        score_user += 1
    if score_user == 5 or score_computer == 5:
        continue
    print("\n###Scores: ")
    print(f"\nComputer: {score_computer}")
    print(f"User: {score_user}")
print("\n")
if score_user > score_computer:
    print("<<<User wins! Game over!>>>")
elif score_user < score_computer:
    print("<<<Computer wins! Congratulations!>>>")
else:
    print("<<<Tie!>>>")
print("\n")