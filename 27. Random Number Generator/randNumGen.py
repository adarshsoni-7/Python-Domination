# 'random'm is a module under which a lot of necessary methods which help us generate the random nunbers in Python. And we here imported from there to here in our code.
import random

# print(help(random)) again it gives us all the methods within the 'random' module.


# Let's have a real life dice into the program.

# dice_num = random.randint(1, 6) here as you can see, we use .randint(starting_num, ending_num) in which both starting and ending numbers are inclusive which generates any number in between 1 & 6.

# print(dice_num)


# We can have any random numbers between 0 and 1 using .random().

# print(random.random()) gives like 0.112233... and so on.


# Let's have a look at some useful 'random' module methods:

# options = ("Rock", "Paper", "Scissors")
# print(random.choice(options)) here if we have to choose from given options, we use .choice() method which then gives any random option from the given choices.


# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]

# What if we have to show the cards to our opponent by shuffling this all.... Well, that's exactly the .shuffle() is for.
# random.shuffle(cards)
# print(cards)


# Let's have a random number generator machine.


start_num = int(input("Enter the starting number(should be > 0): "))
end_num = int(input("Enter the ending number(should be <= 100): "))

genrated_rand_num = random.randint(start_num, end_num)
guessed_num = int(input("Enter the correct generated random number: "))

while genrated_rand_num != guessed_num:
    if guessed_num < genrated_rand_num:
        print(
            "Your numeber was smaller than generated one. Better luck next time :(")
        guessed_num = int(input("Enter the correct generated random number: "))

    elif guessed_num > genrated_rand_num:
        print("Your number was greater. Better luck next time :(")
        guessed_num = int(input("Enter the correct generated random number: "))

print("Congratulations! You caught your number :)")


#                               =====================   Explaination with Warning   ========================

# Now the important concepts are about to come infact from here it has started so keep your entire focus to understand what and how the code works and practise them accordingly too since before we build the skyscraper, we strengthen the base.


# 1. We generated the starting and ending number.
# 2. Then I generate random number as well as guessed number.
# 3. Then I ran a loop untill we will catch the correct random number. Also, we were giving ourselves small hints to help reaching our number.
# 4. Once we'll have our correct number, we ended with a meaningful message. Carefull!!!!! we printed the message outside the while loop.


#                               =====================   Task to do   ========================

# 1. In this same project, add a array of guessing numbers and set a limit of like 4-5 guesses and after that print some message like you have used all your chances now choose next time again.
# 2. Try to alter the condition when we are close to that random number as well as so far to the same.
# 3. Try to count all the guesses in a variable and print it or direct print the length of array of guessing numbers.