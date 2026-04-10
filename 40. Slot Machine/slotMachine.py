# Python Slot Machine

import random

def spin_row():
    symbols = ['🍒',  '🍉',  '🍋',  '🔔', '🌟']

    return [random.choice(symbols) for _ in range(3)]
     
     

def print_row(row):
    print("  | ".join(row))
    print()

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet  * 2

        elif row[0] == '🍉':
            return bet * 4

        elif row[0] == '🍋':
            return bet * 5

        elif row[0] == '🔔':
            return bet * 8

        elif row[0] == '🌟':
            return bet * 10 

    return 0
     


def main():
    balance = 100

    print("**************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 🌟")
    print("**************************")

    while balance > 0:
        if(balance > 1):
            print(f"Current balance : {balance} rupees.")

        else:
            print(f"Current balance : {balance} rupee.")


        bet = input("What will be your betting amount: ")

        if not bet.isdigit():
            print("Kindly mention the valid amount.")
            continue

        bet = int(bet) # Once the valid amount has mentioned, type-cast it to 'int'

        
        if bet > balance:
            print("Insufficient Funds!")
            continue

                  
        if bet <= 0:
            print("Invalid amount!")
            continue


        balance -= bet


        row = spin_row()

        print("Spinning.... \n")

        print_row(row)

        payout = get_payout(row, bet)


        if payout > 0:
            print(f"You won! {payout}")

        else:
            print(f"Unfortunately, you lose! {bet}")

        balance += payout


        play_again = input("Do you wanna play again (Y/N) ?")

        if not play_again.lower() == 'y':
            print("Thanks for playing. Better luck next time!")
            break
 



if __name__ == '__main__':
    main()





# 🧠 What this program is
# A simple slot machine game
# User starts with a balance
# Bets money → spins → either wins or loses
# Game continues until user exits or balance becomes 0


# 🎰 Core flow of the program
# Start with ₹100
# Ask user for bet
# Spin random symbols
# Check result
# Update balance
# Repeat


# ⚙️ Function: spin_row()
# Contains list of symbols: 🍒 🍉 🍋 🔔 🌟
# Picks 3 random symbols
# Returns a list of 3 items

# 👉 Key idea:

# Loop runs 3 times
# Each time → random symbol is chosen


# 🖨️ Function: print_row(row)
# Takes the row (list of symbols)
# Joins them with " | "
# Displays output like:
# 🍒 | 🍉 | 🍋
# 💰 Function: get_payout(row, bet)
# Checks if all 3 symbols are same

# 👉 If match:

# 🍒 → 2x bet
# 🍉 → 4x bet
# 🍋 → 5x bet
# 🔔 → 8x bet
# 🌟 → 10x bet (intended, but bug exists ⚠️)

# 👉 If no match:

# Returns 0


# 🧠 Main Function (Heart of program)
# Initializes balance = 100
# Shows welcome message

# 🔁 Game loop (while balance > 0)
# Runs continuously until:
# balance becomes 0
# user exits

# 💵 Taking user input (bet)
# Takes input as string
# Checks:
# must be digits
# must be ≤ balance
# must be > 0

# 👉 Converts to integer after validation

# 💸 Balance update (before spin)
# Bet amount is deducted first
# Simulates real gambling

# 🎰 Spinning logic
# Calls spin_row()
# Displays result using print_row()

# 🏆 Checking result
# Calls get_payout(row, bet)
# Stores result in payout

# 📊 Win / Lose logic
# If payout > 0:
# User wins
# Print winnings
# Else:
# User loses
# Print loss message

# 💰 Final balance update
# Adds payout back to balance

# 👉 If win → balance increases
# 👉 If lose → balance already reduced

# 🔁 Play again logic
# Asks user: Y/N
# If not 'y' → break loop
# Ends the game


# 🧠 Key Concepts You Must Remember
# random.choice() → generates randomness
# range(3) → controls repetition
# Functions return values → main updates balance
# Input validation prevents crashes