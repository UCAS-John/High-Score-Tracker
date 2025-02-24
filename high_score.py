import csv

PATH = "high_score.csv"

# Locklin
def check_file():
    raise NotImplementedError

# John
def load():
    high_score = {}
    try:
        with open(PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                high_score[row["name"]] = row["score"]
    except Exception as e:
        print(f"Error loading: {e}")
        return None
    
    return high_score

# John
def update():
    high_score = load()
    fieldnames = ["name", "score"]
    try:
        with open(PATH, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow
    except Exception as e:
        print(f"Error update high score: {e}")
        return False
    
#Eli
def display_score():
    raise NotImplementedError

# Use this to test your function
if __name__  == "__main__":
    pass