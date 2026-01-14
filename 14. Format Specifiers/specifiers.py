# Format specifiers are patterns used within Python's string formatting tools to define how individual values should be presented. They come after a colon (:) in a replacement field and are part of Python's string formatting mini-language.

# Here are some common format specifiers and their meanings:


price1 = 123.322222
price2 = 123.3323
price3 = -123.12


print("=================================================================")
print(f" Price is now {price1:.2f}")  # Output: 123.32 (fixed-point notation with 2 decimal places)
print(f" Price is now {price1:.3f}")  # Output: 123.322 (fixed-point notation with 3 decimal places)
print(f" Price is now {price1:.4f}")  # Output: 123.3222 (fixed-point notation with 4 decimal places)
print("=================================================================")


#                              ================================= Important Note =================================

# Rounding Behavior: Python uses "round half to even" (also known as "bankers' rounding") for rounding floating-point numbers. This means that when a number is exactly halfway between two possible rounded values, it rounds to the nearest even number. So don't confuse this with always rounding up.





print(f"After right-aligned the price is {price1:10}")  # Output: 123.3323 with 10 spaces (default is right-aligned)
print(f"After right-aligned the price is {price1:>10}(above and this is same)")  # Output:  123.3323 with 10 spaces (right-aligned)
print(f"After left-aligned the price is {price1:<10}") # Output: 123.3323 with 10 spaces (left-aligned)
print(f"After center-aligned the price is {price1:^10}") # Output:  123.3323  with 10 spaces (center-aligned)

print(f"After leading zeros the price is {price1:010}") # Output: 0000123.3323 with leading zeros to fill width of 10. But here the total width is more than 10, so no leading zeros are added.

print(f"After leading zeros the price is {price2:010}") # Output: 0000123.3323 with leading zeros to fill width of 10
print(f"After leading zeros the price is {price3:010}") # Output: -000123.12 with leading zeros to fill width of 10


print("=================================================================")





big_amount = 323333.25858
print(f"The big amount is {big_amount:,}")  # Output: 323,333.26 (with commas as thousands separators)
print(f"The big amount is {big_amount:,.2f}")  # Output: 323,333.26 (with commas and 2 decimal places)



print("=================================================================")





#                        =========================================== Important Concepts to learn =================================== 

# f string = formatted string literals, introduced in Python 3.6, allow you to embed expressions inside string literals, using curly braces {} as we used recently in the sliccode.