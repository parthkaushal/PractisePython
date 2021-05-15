n = int(input("Please enter a number: "))
i = 2
isPrime = True

while (i < n):
    if (n % i == 0):
        isPrime = False
        break
    i += 1

if(isPrime):
    print("Number is prime")
else:
    print("Number is not prime")