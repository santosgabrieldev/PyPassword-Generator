#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator! \('-')/")
hard_easy = input("Do you want a 1.Simple or a 2.Hard password? ")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

if hard_easy == "1":
    password = ""

    for char in range(1 , nr_letters + 1):
        password += random.choice(letters)

    for char in range(1 , nr_symbols + 1):
        password += random.choice(symbols)

    for char in range(1 , nr_numbers + 1):
        password += random.choice(numbers)

    print("Your password is:",password)
    print("Thanks for using our PyPassword Generator! Have a nice day! \(^-^)/")

    ''' OR
print("Your password is: ")
for letter in range(0, nr_letters):
    letter = (random.choice(letters))
    print(letter, end="") 
for symbol in range(0, nr_symbols):
    symbol = (random.choice(symbols))
    print(symbol, end="")
for number in range(0, nr_numbers):
    number = (random.choice(numbers))
    print(number, end="")
'''

else:

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    password_list = [] #generating a list

    for x in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))
    for x in range(1, nr_symbols + 1):
        password_list.append(random.choice(symbols))
    for x in range(1, nr_numbers + 1):
        password_list.append(random.choice(numbers))    

    #shuffling the characters
    random.shuffle(password_list)

    #Turning list back to string
    password = ""
    for x in password_list:
        password += x
    print(f"Your Hard Level password is: {password}")
    
    print("Thanks for using our PyPassword Generator! Have a nice day! \(^-^)/")

'''
☕ 
--> IG : gabrielsantosdev <--
--> GitHub: santosgabrieldev <--
--> 01/10/21 <--
☕ 
'''