# Alishya 

import random
def play_game():
    score = 0
    comp_score = 0
    while True:
        computer = ['rock', 'paper', 'scissors']
        user = input('Type in your choice(rock, paper, or scissors): ')
        computer_choice = random.choice(computer)
        print('The computer chose .......\n', computer_choice)
        if computer_choice == 'rock' and user == 'rock':
            print('This was a tie')
        elif computer_choice == 'rock' and user == 'paper':
            print('You won this round')
            score+=1
        elif computer_choice == 'rock' and user == 'scissors':
            print('The computer won this round')
            comp_score+=1
        elif computer_choice == 'paper' and user == 'paper':
            print('This was a tie')
        elif computer_choice == 'paper' and user == 'rock':
            print('The computer won this round')
            comp_score+=1
        elif computer_choice == 'paper' and user == 'scissors':
            print('You won this round.')
            score+=1
        elif computer_choice == 'scissors' and user == 'scissors':
            print('This is a tie.')
        elif computer_choice == 'scissors' and user == 'paper':
            print('The computer won this round')
            comp_score+=1
        elif computer_choice == 'scissors' and user == 'rock':
            print('You won this round,')
            score+=1
        else:
            print('That is not one of the options')
        
        choice = input('Would you like to exit the game? y/n\n')
        if choice == 'y':
            complete_score = ('Your final score is:',score)
            comp_complete_score = ('The computers final score is:', comp_score)
            print(complete_score,'\n', comp_complete_score )
            return score
        else:
            continue



# Use this to test your function
if __name__  == "__main__":
    play_game()