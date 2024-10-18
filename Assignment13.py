
# Ask user to enter a string
input_string= input("Enter a string: ")

# convert input to lowercase
input_string = input_string.lower()

# initialize a variable to true
is_palindrome = True

# Use a loop to compare characters from both end of the string
if input_string.isalpha():

    for i in range(len(input_string) // 2):
     if input_string[i] != input_string[-(i + 1)]:
        is_palindrome = False

    if is_palindrome:
        print(" The string is a palindrome")

    else:
     print(" The string is not a palindrome")

else:
 print("Error: Not a string")


