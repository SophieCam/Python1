#input
currency1 = float(input("Enter an amount in $USD: "))

#process and convert currency 1 into EUR using a fixed exchange rate
currency2 = float(currency1 * 0.899)

#output
print("The converted amount from USD to EUR is:  ", currency2)