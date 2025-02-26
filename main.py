from game import play_game
from high_score import display_top_ten, update
import csv

#We have to display the user's username and their score when we display the top 10 scores
    
info = {}

def user_profiles():
    info = {}
    username = input('What is your username: ')
    password = input('What is your password')
    if username in info and info[username] == password:

    #else:
        print('You don\'t alreday have an account.\n Would you like to add this account? (y/n)')

    info[username] = password

    pass

def main():
    title = "Welcome to a rock paper scissors game!"
    title_case_string = title.title()
    print(title_case_string)

    
    while True:

        log_in_or_exit = input('What do you want to do?\n1. Log into an account\n2. Exit\nChoice:')
        match log_in_or_exit:
            case '1':
                username = input('What is your username: ')
                password = input('What is your password: ')
                info[username] = password
                print(info)
                break
            case '2':
                print('Thankyou for playing!')
                exit()
            case _:
                print('That is not an option. Try again')
                continue
        
    while True:
        choice = input('What would you like to do?\n1. Play Game\n2. Display top 10 scores\n3. Log out\nChoice: ')

        match choice:
            case '1':
                play_game()
            case '2':
                display_top_ten()
            case '3':
                print("You have logged out!")
                main()
            case _:
                print("That is not an option")
                continue

if __name__ == "__main__":
    main()