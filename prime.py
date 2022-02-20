number = input("Enter a number: ")
number = int(number)
not_prime = False
if number > 1:
    for value in range(2, number):
        if (number % value) == 0:
            not_prime = True
            break

if not_prime:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")
