import random
import string
length=int(input("enter length:"))
pwd=" "
characters= string.digits + string.asci_letters+ string.puncutation
for i in range(length):
    pwd+=random.choice(characters)
print("password is",pwd)
