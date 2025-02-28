# Alishya 

#This helps the computer randomly pick one of the choices
import random

#This is the function that plays the rock paper scissors game 
def play_game():

    #These take care of the players score
    score = 0

    while True:
        computer = ['rock', 'paper', 'scissors']
        user = input('\nType in your choice(rock, paper, or scissors): ').strip().lower()
        computer_choice = random.choice(computer)
        
        if computer_choice == 'rock' and user == 'rock':
            print('The computer chose .......\n', computer_choice)
            print('This was a tie.(No points are given)\n')
            continue
            
            
        elif computer_choice == 'rock' and user == 'paper':
            print('The computer chose .......\n', computer_choice)
            print('You won this round\n')
            score+=1
            continue
            
        elif computer_choice == 'rock' and user == 'scissors':
            print('The computer chose .......\n', computer_choice)
            print('The computer won this round\n')
            print(f'Your final score is: {score}')
            return score

            
        elif computer_choice == 'paper' and user == 'paper':
            print('The computer chose .......\n', computer_choice)
            print('This was a tie.(No points are given)\n')
            continue
            
        elif computer_choice == 'paper' and user == 'rock':
            print('The computer chose .......\n', computer_choice)
            print('The computer won this round\n')
            print(f'Your final score is: {score}')
            return score
        
            
        elif computer_choice == 'paper' and user == 'scissors':
            print('The computer chose .......\n', computer_choice)
            print('You won this round.\n')
            score+=1
            continue
            
        elif computer_choice == 'scissors' and user == 'scissors':
            print('The computer chose .......\n', computer_choice)
            print('This is a tie.(No points are given)\n')
            continue
        elif computer_choice == 'scissors' and user == 'paper':
            print('The computer chose .......\n', computer_choice)
            print('The computer won this round\n')
            print(f'Your final score is: {score}')
            return score
            
        elif computer_choice == 'scissors' and user == 'rock':
            print('The computer chose .......\n', computer_choice)
            print('You won this round.\n')
            score+=1
            continue
        else:
            print('That is not one of the options. Try again...\n')
            continue
        
    


# Use this to test your function
if __name__  == "__main__":
    play_game()