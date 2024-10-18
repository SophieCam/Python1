#Initialize a flag for input validation
valid_input = False

#Loop until valid input is received
while not valid_input:
    user_input = input("Enter a positive number: ")

    #check if the input is a positive number
    if user_input.isdigit():
        num = int(user_input)
        if num > 0:
            valid_input = True
        else:
            print("Please enter a positive number.")
    else:
        print("That's not a valid number. Please try again! ")

#Generate the Collatz Sequence
print("Collatz Sequence: ")

while num != 1:
    print(num, end=" ")
    if num % 2 == 0:
        num //= 2  #if even, divide by 2
    else:
        num = 3 * num +1
print(num)

