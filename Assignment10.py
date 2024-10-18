#Input/Prompt user to enter their age
age_input = input("Please enter your age: ")

#check if input is a number and not an empty string via validation
if age_input.isdigit():
    age = int(age_input) #coverting string to int and storing it in age variable
    #ensure the age is positive
    if age > 0:
        #classify the age into categories
        if age <18:
            print("Minor")
        elif 18 <= age <= 65:
            print("Adult")
        else:
            print("Senior Citizen")
    else:
        print("Error: Age must be a positive integer. ")
else:
    print(" Error: Invalid input. Please enter a positive integer. ")