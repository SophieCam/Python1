# Input/Prompt user to enter their marks for three subjects
# Check for valid input and range 0-100

 # Subject 1
valid_input = False
while not valid_input:
     Subject1_input = input("Please enter your mark for Subject 1: ")
     if Subject1_input.isdigit():
         s1 = int(Subject1_input)
         if 0 <= s1 <= 100:
             valid_input = True
         else:
             print("Error: Mark must be between 0 and 100. Please try again.")
     else:
         print("Error: The input is not a valid number. Please try again.")

 #Subject 2
valid_input = False
while not valid_input:
    Subject2_input = input("Please enter your mark for Subject 2: ")
    if Subject2_input.isdigit():
        s2 = int(Subject2_input)
        if 0 <= s2 <= 100:
            valid_input = True
        else:
            print("Error: Mark must be between 0 and 100. Please try again.")
    else:
        print("Error: The input is not a valid number. Please try again.")

 # Subject 3
valid_input = False
while not valid_input:
    Subject3_input = input("Please enter your mark for Subject 3: ")
    if Subject3_input.isdigit():
        s3 = int(Subject3_input)
        if 0 <= s3 <= 100:
            valid_input = True
        else:
            print("Error: Mark must be between 0 and 100. Please try again.")
    else:
        print("Error: The input is not a valid number. Please try again.")

# Calculate the average
average = (s1 + s2 + s3) / 3

# Classify the marks into grade categories
if average >= 90:
    print("Calculated grade is A")
elif 80 <= average < 90:
    print("Calculated grade is B")
elif 70 <= average < 80:
    print("Calculated grade is C")
elif 60 <= average < 70:
    print("Calculated grade is D")
else:
    print("Calculated grade is F")