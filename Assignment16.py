
def is_prime (num):



    if num <= 1:
        #print("Is not a prime")
        return False
    else:
        for i in range ( 2, int(num ** 0.5) +1):
            if num % i == 0:
                return False
        else:
           # print("Is prime")
            return True

number = int(input("Enter a number: "))

if is_prime(number):
    print("This is a prime number")
else:
    print("This is not a prime number")