#Input for 3 different variables

principal =float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))

#Processing the simple interest

simple_interest =  (principal * rate * time) / 100

#this is the output for simple interest
print("Simple Interest is: ", simple_interest)