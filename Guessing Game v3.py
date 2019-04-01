import random

random_number = random.randint(1,10)

while True:
    user = int(input('Pick a number from 1 to 10: '))
    if user < random_number:
        print('Too Low')
    elif user > random_number:
        print('Too High')
    else:
        print('You won!!!')
        play_again = input('Do you wan to play again? (y/n)')
        if play_again == 'y':
            random_number = random.randint(1,10)
            user = None
        else:
            print('Thank you for playing!!')
            break
