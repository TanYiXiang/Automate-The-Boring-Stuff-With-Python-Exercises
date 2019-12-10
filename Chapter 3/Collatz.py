def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return (3 * number) + 1


userInput = input()
try:
    collatzNumber = int(userInput)
    print(collatzNumber)
    while collatzNumber != 1:
        collatzNumber = collatz(collatzNumber)
        print(collatzNumber)
except ValueError:
    print('Please enter an integer value')
