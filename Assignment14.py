#method 1
#def power(base, exponent):
    #return base * power(base, exponent -1)

#method 2 with checks
def power (base, exponent):
    if exponent == 0:  # checking any number to the power of 0
        return 1
    elif exponent < 0: # checks for negative exponents
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

print(power(2, 3))
print(power(5, 0))
print(power(2, -3))