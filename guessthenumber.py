# This game lets the user guess the a number which the computer has selected
import random

secret_number = random.randint(0, 16)

print('Guess the number in the range of 0 to 16')
for n in range(1, 6):
    guess = int(input())
    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    elif guess == secret_number:
        print('Congratulation!, you have guess correctly')
else:
    print('I was thinking of ('+ str(secret_number) +')')

