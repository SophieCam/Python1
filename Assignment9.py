
from time import process_time_ns
from xml.sax.saxutils import prepare_input_source

#Promt the user to enter a single character
char_input = input("Please enter a single character: ") #no need to convert type since input output is already a string

#Check if the input is exactly one character long and is a letter
if len(char_input) == 1 and char_input.isalpha(): #.isalpha confirms input is a letter
    #checks user input and convert character to lowercase
    char = char_input.lower()

    if char in "aeiou": #think of in as "is" so if the character is a part of this string...then do something
        print(" The character is a vowel. ")
    else:
        print(" The character is a consonant. ")
else:
    #handle cases where input is not a single letter
    if len(char_input) != 1:
        print("Error: Please enter only one character. ")
    else:
        print(" Error: The input is not a letter")


