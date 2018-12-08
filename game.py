import random

attempts = 3
secret_number = random.randint(1, 10)

name = input('Hi, Whats your name? \n')
print ("Well", name, "i am thinking of a number between 1 and 10")

for attempt in range(attempts):
    guess = int(input('Take a guess: '))

    if guess < secret_number:
        print('Higher...')
    elif guess > secret_number:
        print('Lower...')
    else:
        print()
        print('You guessed it! The number was ', secret_number)
        print('You guessed it in', attempts, 'attempts')

        break

if guess != secret_number:
    print()
    print('Sorry you reached the maximum number of tries')
    print('The secret number was', secret_number)
