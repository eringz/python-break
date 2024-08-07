# Write function named collatz() that has one parameter named number.
# if number is even should print number // 2 and return this value
# if number is odd should print and return 3 * number + 1
# let the user type in an integer and that ceeps calling collatz on that number until the function returns to val 1

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

number = int(input('Enter a number: '))

while True:
    if number != 1:
        number = collatz(number)
    else:
        break