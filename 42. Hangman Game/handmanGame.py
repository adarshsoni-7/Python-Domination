# This is a simple implementation of the Hangman game in Python. The game selects a random word from a predefined list and allows the user to guess letters until they either guess the word correctly or run out of guesses. The game also displays a visual representation of the hangman based on the number of wrong guesses.
import random

words = ["apple", "banana", "cherry", "grape", "orange", "strawberry", "watermelon"]


hangman_art = {
    0: (" ",
        "  ",
        "  "),
    1: (" ○ ",
        "  ",
        "  "),
    2: (" ○ ",
        " | ",
        "  "),
    3: (" ○ ",
        "/| ",
        "  "),
    4: (" ○ ",
        "/|\\",
        "  "),
    5: (" ○ ",
        "/|\\",
        "/  "),
    6: (" ○ ",
        "/|\\",
        "/ \\")
}



def display_man(wrong_guesses):
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("************")



def display_hint(hint):
    print("  ".join(hint))
    print()                                                                          



def display_answer(answer):
    print("  ".join(answer))


def main():
    answer = random.choice(words) # Select a random word from the list
    hint = ["_"] * len(answer) # Create a hint with underscores for each letter in the answer
    wrong_guesses = 0 # Initialize the number of wrong guesses to 0
    guessed_letters = set() # Create a set to keep track of guessed letters

    is_running = True # Set a flag to indicate that the game is running


    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        
        guess = input("Enter a letter: ").lower()
        print()


        if len(guess) != 1 or not guess.isalpha(): # Check if the input is a single letter
            print("Invalid input.")
            print()
            continue

        if guess in guessed_letters: # Check if the letter has already been guessed
            print(f"{guess} is already guessed.")
            print()
            continue

        if guess in answer:
            for i in range(len(answer)): # Check each letter in the answer and update the hint if it matches the guess
                if answer[i] == guess: # If the letter at index i in the answer matches the guess, update the hint at index i to show the guessed letter
                    hint[i] = guess

            guessed_letters.add(guess) # Add the guessed letter to the set of guessed letters

        else:
            wrong_guesses += 1 # Increment the number of wrong guesses if the guess is not in the answer



        if "_" not in hint and wrong_guesses != 6:            
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You guessed the word!")
            is_running = False
       

        elif wrong_guesses == 6:
            display_man(wrong_guesses)
            print(f"Game Over! You ran out of guesses. Your answer was: {answer}")
            is_running = False



if __name__ == "__main__":
    main()



#                                         ============ Explanation ============

# 1. The game starts by importing the random module and defining a list of words that can be used in the game.

# 2. A dictionary called hangman_art is created to store the visual representation of the hangman based on the number of wrong guesses.

# 3. The display functions are defined to show the hangman, the hint, and the answer to the user.

# 4. The main function is defined to run the game. It selects a random word from the list, initializes the hint and wrong guesses, and sets a flag to indicate that the game is running.

# 5. The game enters a while loop that continues until the game is over. Inside the loop, the hangman and hint are displayed, and the user is prompted to enter a letter.

# 6. The input is validated to ensure it is a single letter and has not been guessed before. If the guess is correct, the underscore is replaced with the guessed letter. If the guess is incorrect, the number of wrong guesses is incremented.

# 7. The game checks if the user has guessed the word correctly or if they have run out of guesses. If the user wins, a congratulatory message is displayed. If the user loses, a game over message is displayed along with the correct answer.