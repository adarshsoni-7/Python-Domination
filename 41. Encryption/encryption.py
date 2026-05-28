# This is a simple encryption and decryption program that uses a random key to substitute characters in the input text. The program first creates a list of characters that includes spaces, punctuation, letters, and digits. It then creates a copy of this list to serve as the key for encryption. The key is shuffled randomly to create a unique mapping of characters.

import random
import string


chars = " " + string.punctuation + string.ascii_letters + string.digits

chars = list(chars)

key = chars.copy()


random.shuffle(key)



#ENCRYPT


raw_text = input("Enter the text to be encrypted: ")
encrypted_text = ""


for letter in raw_text:
    index = chars.index(letter) # Find the index of the letter in the original character list
    encrypted_text += key[index] # Substitute the letter with the corresponding character in the key based on the index in encrypted_text


print(f"Original Text: {raw_text}")
print(f"Encrypted Text: {encrypted_text}")



#DECRYPT


encrypted_text = input("Enter the text to be encrypted: ")
raw_text = ""


for letter in encrypted_text:
    index = key.index(letter) # Find the index of the letter in the original key list
    raw_text += chars[index] # Substitute the letter with the corresponding character in the original character list based on the index in raw_text



print(f"Original Text: {encrypted_text}")
print(f"Decrypted Text: {raw_text}")





#                                   =========================== Explanation (Encryption) ===========================

# 1. The program starts by importing the necessary modules: `random` for shuffling the key and `string` for accessing predefined character sets.
# 2. A string of characters is created that includes a space, punctuation, letters (both uppercase and lowercase), and digits. This string is then converted into a list for easier manipulation.
# 3. A copy of the original character list is made to serve as the key for encryption. The key is then shuffled randomly using `random.shuffle()`, creating a unique mapping of characters.
# 4. The user is prompted to enter the text they wish to encrypt. An empty string is initialized to store the encrypted text.
# 5. The program iterates through each character in the input text, finds its index in the original character list, and appends the corresponding character from the shuffled key to the encrypted text.
# 6. The original and encrypted texts are printed to the user.



#                                   =========================== Explanation (Decryption) ===========================

# We did the same thing as encryption but in reverse. We take the encrypted text and for each character, we find its index in the key and then substitute it with the corresponding character from the original character list to reconstruct the original text.