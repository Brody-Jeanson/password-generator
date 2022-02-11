import string
from unicodedata import numeric 
import random
lowercaseLetters = string.ascii_lowercase
uppercaseLetters = string.ascii_uppercase
numbers = string.digits
specialCharacters = string.punctuation

characters = [lowercaseLetters + uppercaseLetters + numbers + specialCharacters]

def generatepassword():
    passwordLength = int(input('Enter password length: '))
    random.shuffle(characters)
    password = []
    for i in range(passwordLength):
        password.append(random.choices(characters))
    random.shuffle(password)
    print(''.join(password))

generatepassword()
