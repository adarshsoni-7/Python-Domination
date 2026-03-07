# In this program, we will create a shopping cart program.


foods = []
prices = []
total = 0


while True:
    food = input("Please enter the name of food you want (q to quit): ")
    
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = input("Enter the price of the food (in INR): ")
        prices.append(price)


print("---------------   YOUR CART  ---------------")
 

if len(foods) == 0:
    for food in foods:
        print(food, end=" ")
    else:
        print("There is no item to show here.")

print()


for price in prices:
    print(f"The total price of your shopping is: {price}", end=" ")



print("---------------  END OF SHOPPING LIST  ---------------")








#                                                   ================  Task to do =====================


# 1. Check the code by converting only price input to int and check why not error shows but why code does unexpected behaviour
# 2. Add a discount coupon if anyone's total price > 2000 for 20% and more........