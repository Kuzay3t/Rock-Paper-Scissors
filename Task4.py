import random

# introducing the game to the user
print("Welcome to Rock-Paper_Scissors game")

while True:
    users_choice = int(input("""What operation do you want to perform?
                             1. Play game 
                             2. Quit game 
                             \n """))
    if users_choice == 2:
        print("Thank you for playing the game")
        break
    elif users_choice == 1:
    # collecting input from the user
        users_choice = int(input("""
                                Input the corresponding number for the choice you want to make
                                1. Rock
                                2. Paper
                                3. Scissors
        """))

        # tracking the user's score and the ciqmputer's score                        
        users_score = 0
        computer_score = 0
        choice = { 1: "Rock",  2:"Paper",  3 : "Scissors"}

        computer_choice = random.randint(1,3)

        # comparing the user's choice with the computer's choice to determine the winner
        while True:
            if users_choice == computer_choice:
                print("It's a tie")
                break
            elif users_choice == 1:
                if computer_choice == 2:
                    print(f"Your choice is {choice[users_choice]}  and the computer's choice is {choice[computer_choice]}")
                    print("You lose")
                    users_score += 0
                    computer_score += 1
                    print(f"Your score is {users_score} and the computer's score is {computer_score}")
                    break
                else:
                    print(f" Your choice is {choice[users_choice]}  and the computer's choice is {choice[computer_choice]}")
                    print("You win")
                    users_score += 1
                    computer_score += 0
                    print(f"Your score is {users_score} and the computer's score is {computer_score}")
                    break
            elif users_choice == 2:
                if computer_choice == 1:
                    print(f" Your choice is {choice[users_choice]}  and the computer's choice is {choice[computer_choice]}")
                    users_score += 1
                    computer_score += 0
                    print(f"Your score is {users_score} and the computer's score is {computer_score}")
                    break
                else:
                    print(f" Your choice is {choice[users_choice]}  and the computer's choice is {choice[computer_choice]}")
                    print("You lose")
                    users_score += 0
                    computer_score += 1
                    print(f"Your score is {users_score} and the computer's score is {computer_score}")
                    break
            elif users_choice == 3:
                if computer_choice == 1:
                    print(f" Your choice is {choice[users_choice]}  and the computer's choice is {choice[computer_choice]}")
                    print("You lose")
                    users_score += 0
                    computer_score += 1
                    print(f"Your score is {users_score} and the computer's score is {computer_score}")
                    break
                else:
                    print(f" Your choice is {choice[users_choice]}  and the computer's choice is {choice[computer_choice]}")
                    print("You win")
                    users_score += 1
                    computer_score += 0
                    print(f"Your score is {users_score} and the computer's score is {computer_score}")
                    break
    else:
        print("Invalid choice")