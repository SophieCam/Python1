

#Get user input for number of rows and the character to use in the pattern
rows = int(input("Enter the number of rows: "))
char = input("Enter the character to use for the pattern: ")

#2 Nested loops to print the right triangle pattern
for i in range (1, rows +1):
    for j in range(i):
        print (char, end= " ")
    print()


