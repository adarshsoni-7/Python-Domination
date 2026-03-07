# Here, we'll cover a hands-on project for the dictionaries in Python.


cafe_menu = {"Cold Coffee": 99,
             "Tea": 15,
             "Maggie": 59,
             "Momos": 49,
             "French-Fries": 99,
             "Lava-Cake": 99,
             "Cheese-Burger": 99}


cart = []
total_price = 0


for name, price in cafe_menu.items():
    wants = input(f"Have some {name} of {price}: (y/n/q): ")
    if wants.lower() == "y":
        cart.append(name)
        total_price += price
    elif wants.lower() == "q":
        break  
        
print("===== This is your cart ======")

if len(cart) == 0:
    print("No item")

for items in cart:
    print(items)
    
    
if len(cart) > 0:
    print(f"You have to pay {total_price}/- only.")
        
else:
    print("You did not order anything.")
    
    
#                               ===================== Explaination ================================

# 1. We declared cafe_menu in which we have our junk food lists with their price.
# 2. Then we have a cart in which all the selected items is storing using .append() as we discussed previously.
# 3. Then the total_price basically have the total price of all selected items.
# 4. We ran a loop and store the selected items in the lists along with adding their price in total_price.
# 5. Eventually, we printed the cart with their total price.