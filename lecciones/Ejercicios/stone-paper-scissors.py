#Exercise: Stone, Paper and Scissors in Python applying conditionals, loops and functions
#The code needs improvements: try-catch for possible input errors..
#It will continue at twitch.tv/juliancampos_es
import random

def options():
    
    options = ('Stone','Paper','Scissors')
    print('The options are: ')
    print('1. Stone')
    print('2. Paper')
    print('3. Scissors')
    
    user_option = int(input('Please, select your option with the number: '))
    
    #check if the input doesn't match with the options
    #if not -> return None and None to continue the loop
    if user_option != 1 and user_option != 2 and user_option != 3:
        print('The input is not correct')
        return None, None
    
    user_option -= 1
    user_option = options[user_option]
    
    computer_option = random.choice(options)
    
    return user_option, computer_option

def check_results(user_option, computer_option):
    
    if user_option == computer_option:
        return 'Draw'
    
    match user_option:
        case 'Stone':
            if computer_option == "Scissors":
                print('Stone wins against Scissors')
                print('User wins')
                return 'Win'
            else:
                print('Stone loses against Paper')
                print('User loses')
                return 'Lose'
        case 'Paper':
            if computer_option == 'Stone':
                print('Paper wins against Stone')
                print('User wins')
                return 'Win'
            else:
                print('Paper loses against Scissors')
                print('User loses')
                return 'Lose'
        case 'Scissors':
            if computer_option == 'Paper':
                print('Scissors wins against Paper')
                print('User wins')
                return 'Win'
            else:
                print('Scissors loses against Stone')
                print('User loses')
                return 'Lose'

def start_game():
    round_game = 0
    computer_score = 0
    user_score = 0
    finish_game = False 
    user_option = ''
    computer_option = ''
    
    print(' ')
    print('-- Welcome to the classic game Stone, Paper and Scissors --')
    print(' ')
    print('You are going to play against the computer, the rules are very simple:')
    print('Each round,  you can choise one option: 1. Stone, 2. Paper and 3. Scissors')
    print('The computer will take a random option and we will check who is the winner' )
    print(' ')
    print('-- Stone wins against the Scissors')
    print('-- Scissors wins against the Paper')
    print('-- Paper win against the Stone')
    print(' ')
    print('Lets start the game')
    print(' ')
    


    while finish_game == False:
        print('Round: ' + str(round_game))
        print('User score: ' + str(user_score))
        print('Computer score: '+ str(computer_score))
        print(' ')
        
        user_option, computer_option = options()
        result = check_results(user_option, computer_option)
        if user_option == None:
            continue
        
        if result == 'Win':
            user_score += 1
        elif result == 'Lose':
            computer_score += 1  
        elif result == 'Draw':
            print('This round is a draw')
            print(' ')
            
        round_game += 1

        finish_game_input = input('Do you want to continue?(yes or no): ')
        finish_game_input.lower()
        print(' ')
        if finish_game_input == 'yes':
            finish_game = False
        elif finish_game_input == 'no':
            print('Game finished')
            print(' ')
            print('The result is: ')
            print(' ')
            print('You: ' + str(user_score) + ' - Computer: ' + str(computer_score) )
            finish_game = True
        else:
            print('The answer is not correct so... next round! ;-)')
            print(' ')
            finish_game = False
        
    

if __name__ == '__main__':
    start_game()

