import random
import string

chars = string.punctuation+string.digits+string.ascii_letters+" "
chars = list(chars)
key = chars.copy()

random.shuffle(key)
# ENCRYPTION
print_text = input("enter the value to be encrypted: ")
chiper_text=""

for letters in print_text:
    index = chars.index(letters)
    chiper_text += key[index] 

print(f"original letters = {print_text}")
print(f"encrypted letters = {chiper_text}")
#DECRYPTION
chiper_text = input("enter the value to be decrypted: ")
print_text=""

for letters in chiper_text:
    index = key.index(letters)
    print_text += chars[index] 

print(f"encrypted letters = {chiper_text}")
print(f"original letters = {print_text}")