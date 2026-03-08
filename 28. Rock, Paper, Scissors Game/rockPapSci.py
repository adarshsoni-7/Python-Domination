import random
options = ("Rock", "Paper", "Scissors")
score = 0

isRunning = True

while isRunning:

    player_choice = None                      
    computer_chocice = random.choice(options)   

    while player_choice not in options:
        player_choice = input("Enter your choice: ")

    if player_choice == "Rock" and computer_chocice == "Scissors" or player_choice == "Scissors" and computer_chocice == "Paper" or player_choice == "Paper" and computer_chocice == "Rock":
        print(f"You Won! because between {player_choice} and {computer_chocice}, always {player_choice} has more strength than {computer_chocice}.")
        score += 1
    else:
        print("You defeated!")
        score -= 1 if score > 0 else 0

    play_again = input("Want to play again (y/n): ").lower()   

    if play_again == "y":
        isRunning = True
    else:
        isRunning = False
        print(f"You quit the game with a score of {score}. Thanks for playing!")
        
        
        
#                                               ==================== Explanation ====================

# 1. We import the random module to allow the computer to make a random choice.
# 2. We define the options for the game as a tuple: "Rock", "Paper", and "Scissors".
# 3. We initialize the player's score to 0 and set a flag (isRunning) to control the game loop.
# 4. We start a while loop that continues as long as isRunning is True.
# 5. Inside the loop, we initialize player_choice to None and randomly select a choice for the computer.
# 6. We use another while loop to prompt the player for their choice until they enter a valid option.
# 7. We compare the player's choice with the computer's choice to determine the winner and update the score accordingly.
# 8. After each round, we ask the player if they want to play again. If they enter "y", the game continues; otherwise, it ends and displays the final score.




#                                              ==================== Task to do ====================

# 1. Add a feature to keep track of the number of wins, losses, and ties for the player. Careful! You have to write different types of if-else logic for ties.
# 2. Add a feature to allow the player to choose the number of rounds they want to play, and keep track of the score across all rounds.



#                                             ==================== Important Message ====================

# See, from here the concepts gradually become more complex, so I suggest you to try to understand the code and then try to implement the above tasks on your own. If you get stuck, feel free to use my debugging prompts! For Example: you can see there, instead of writing the logic for wins and losses in many if-else block, we merge them into one statement using "or", "and" operators.