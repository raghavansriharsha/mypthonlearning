import random

# selects a random number between 1 and 100
number = random.randint(1,100)
number_of_guesses = 0

while number_of_guesses < 10 :
    guess = input('Guess a Number between 1 and 100:')
    guess = int(guess)
    if(guess == number):
        print('hooray!')
        break 
    else:
        number_of_guesses = number_of_guesses + 1
    if(guess >= number):     
        print('your guess was too high')
    elif(guess <= number):   
        print('your guess was too low')

    if(number_of_guesses == 10):
        print('Oh noooooooooooooo !,The Magic Number was:', number)