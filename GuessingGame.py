import random 
# Guessing Game, where you play against a bot to guess the number it is 'thinking' of 
def game(high_number):
    bot = random.randint(1,high_number)
    tries = 0
    game_over = False
    play_again = True 

    while not game_over:
        userinput = int(input(f'Enter a number between 1 and {high_number} '))
        if bot == userinput:
            tries += 1
            game_over = True
        elif bot < userinput:
            tries += 1
            print('Try a lower number')
        elif bot > userinput:
            tries += 1
            print('Try a higher number')
            
    print(f'You Win, it took you {tries} tries')
    # Offers the user the option to move to next level
    play_again = input('Do you want to go to the next level? ').lower()
    if play_again == 'y' or play_again == 'yes':
        game(high_number + 10)
    else:
        exit()


game(10)
