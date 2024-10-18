year_input = (input("Enter a year: "))
if year_input.isdigit():
    year = int(year_input)

    if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
        print(" Leap Year ")
    else:
        print("Not a Leap Year")

else:
    print(" Error: Invalid input. Please enter a positive integer. ")