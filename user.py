from high_score import write, load

USER_PATH = "user.csv"

def store_user(username: str, password: str) -> None:
    users = load(USER_PATH)
    if username in users:
        print("\nUsername is already used\n")
        return
    
    users[username] = password

    write(USER_PATH, users)

def check_user(username: str, password: str) -> bool:
    users = load(USER_PATH)

    if username in users:
        if password == users[username]:
            return True
    return False