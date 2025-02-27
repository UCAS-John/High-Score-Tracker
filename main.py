from game import play_game
from file import check_file
from high_score import display_top_ten, update
from user import store_user, check_user

def main():
    check_file()
    title = "Welcome to a rock paper scissors game!"
    title_case_string = title.title()
    print(title_case_string)

    
    while True:

        log_in_or_exit = input('What do you want to do?\n1. Log into an account\n2. Sign up\n3. Exit\nChoice: ').strip()

        match log_in_or_exit:
            case '1':
                username = input('What is your username: ').strip()
                password = input('What is your password: ').strip()
                if check_user(username, password):
                    print(f"\nWelcome {username}!\n")
                    break
                else:
                    print("\nInvalid Username or Password\n")
                    continue
            case '2':
                username = input('What is your username: ').strip()
                password = input('What is your password: ').strip()
                if not store_user(username, password):
                    continue
                print(f"\nWelcome {username}\n")
                break

            case '3':
                print('Thankyou for playing!')
                return

            case _:
                print('That is not an option. Try again')
                continue
        
    while True:
        choice = input('What would you like to do?\n1. Play Game\n2. Display top 10 scores\n3. Log out\nChoice: ').strip()

        match choice:
            case '1':
                score = play_game()
                update(name=username, score=score)
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