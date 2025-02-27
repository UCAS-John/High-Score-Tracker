# Alishya 

#This helps the computer randomly pick one of the choices
import random

#This is the function that plays the rock paper scissors game 
def play_game():

    #These take care of the players score
    score = 0

    time = 0
    while True:

        computer = ['rock', 'paper', 'scissors']
        user = input('Type in your choice(rock, paper, or scissors): ')
        computer_choice = random.choice(computer)
        print('The computer chose .......\n', computer_choice)
        if computer_choice == 'rock' and user == 'rock':
            print('This was a tie.(No points are given)')
            time+=1
        elif computer_choice == 'rock' and user == 'paper':
            print('You won this round')
            score+=1
            time+=1
        elif computer_choice == 'rock' and user == 'scissors':
            print('The computer won this round')
            time+=1
        elif computer_choice == 'paper' and user == 'paper':
            print('This was a tie.(No points are given)')
            time+=1
        elif computer_choice == 'paper' and user == 'rock':
            print('The computer won this round')
            time+=1
        elif computer_choice == 'paper' and user == 'scissors':
            print('You won this round.')
            score+=1
            time+=1
        elif computer_choice == 'scissors' and user == 'scissors':
            print('This is a tie.(No points are given)')
            time+=1
        elif computer_choice == 'scissors' and user == 'paper':
            print('The computer won this round')
            time+=1
        elif computer_choice == 'scissors' and user == 'rock':
            print('You won this round.')
            score+=1
            time+=1
        else:
            print('That is not one of the options. Try again...')
            continue
        
        if time == 5:
            print(f'Your final score is: {score}')
            return score
        else:
            continue
    


# Use this to test your function
if __name__  == "__main__":
    play_game()