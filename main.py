from game import play_game
from high_score import *
import csv

def user_profiles():
    info = {}
    username = input('What is your username: ')
    password = input('What is your password')
    if username in info and info[username] == password:

    else:
        print('You don\'t alreday have an account.\n Would you like to add this account? (y/n)')

    info[username] = password

    pass


def main():
    title = "Welcome to a rock paper scissors game!"
    title_case_string = title.title()
    print(title_case_string)

    while True:
        choice = input('What would you like to do?\n1. Play Game\n2. Display top 10 scores\n3. Log out')
        match choice:
            case '1':
                name = input("Enter your name: ")
                score = play_game()
                update(name=name, score=score)
            case '2':
                display_score()
            case '3':
                print("Log out")
                return
            case _:
                print("Invalid Choice")
                continue

if __name__ == "__main__":
    main()