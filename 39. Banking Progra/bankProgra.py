def show_balance(balance):
    print(f"Your balance is INR {balance} /-")


def deposit():
    amount = int(input("Enter the amount to be deposited: "))
    print()

    if amount < 0:
        print("That's not a valid amount.")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = int(input("Enter the amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Enter a valid amount.")
        return 0
    else:
        return amount


def main():
    balance = 0
    isRunning = True

    while isRunning:
        print("Banking program")
        print()
        print("***************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit!")
        print()
        print("***************************")

        choice = input("What do you want to do? (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            isRunning = False

        else:
            print("That is not a valid choice.")

    print("Thank You! Have a nice day!")


if __name__ == '__main__':
    main()



#     ======================================== Explaination ==========================================

# 🧠 Step 1: Think of the program as a flow
# The program behaves like a simple banking machine
# Flow is: start → show menu → take input → perform action → repeat
# It keeps running until the user chooses to exit


# 🔁 Step 2: Where execution starts
# Execution begins from the condition checking if the file is run directly
# When true, the main function is called
# This acts as the entry point of your program


# 🧱 Step 3: Entering main function
# A variable called balance is created and initialized to 0
# Another variable isRunning is set to True
# These variables exist only inside main and control the program


# 🔁 Step 4: Loop begins
# A loop runs as long as isRunning is True
# This creates continuous execution (menu keeps appearing)


# 📋 Step 5: Menu display
# The program shows options: show balance, deposit, withdraw, exit
# The user inputs a choice


# ⚙️ Step 6: Decision making based on user input
# Show Balance
# Calls the function to display balance
# Only reads the value, does not change it

# Deposit
# Calls deposit function
# Takes user input
# Validates the amount
# Returns the value
# Main function adds it to balance

# Withdraw
# Calls withdraw function with current balance
# Checks if amount is valid and available
# Returns the value
# Main function subtracts it from balance

# Exit
# Changes isRunning to False
# Loop stops and program ends


# 🔁 Step 7: Loop repetition
# After every action, the menu appears again
# The process repeats until exit is chosen


# 🧠 Step 8: Core concept (most important)
# Balance is the central variable
# All operations depend on it:
# Show → reads balance
# Deposit → increases balance
# Withdraw → decreases balance


# 🔥 Step 9: Function behavior
# Deposit function:
# Takes input
# Validates
# Returns amount
# Withdraw function:
# Takes balance and input
# Validates conditions
# Returns amount
# Functions do not directly change balance
# They return values, and main updates balance


# 💡 Golden rule
# Main function controls everything
# Functions only help perform specific tasks


# ⚡ Final mental model
# Main function = brain (controls flow)
# Balance = memory (stores money)
# Functions = workers (perform tasks)


# 🚀 Outcome of understanding this
# You can modify the program easily
# You can debug similar problems
# You can implement this logic in other languages like C++