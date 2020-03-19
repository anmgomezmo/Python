number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))
    
    if guess == number:
        print('Congratulations, you guessed it.') 
        running = False # This causes the while loop stop 
    elif guess < number:
        print('No, it is a little higher than that')
    else:
        print('No, it is a little lower tha that')
else:
    print('The white loop is over.')
    # Do anything else you want to do here

print('Done')
