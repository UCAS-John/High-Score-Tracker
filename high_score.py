import csv

PATH = "high_score.csv"

# Locklin
def check_file():
    raise NotImplementedError

# John
def load() -> dict:
    high_score = {}
    my_list = []
    try:
        with open(PATH, newline="") as file:
            reader = csv.reader(file, delimiter=",")
            if reader is None:
                return high_score
            for row in reader:
                my_list.append(row)
            if len(my_list) != 2:
                return high_score
            for key, value in zip(my_list[0], my_list[1]):
                high_score[key] = value
    except Exception as e:
        print(f"Error loading: {e}")

    return high_score

# John
def update(name: str, score: int) -> None:
    high_score = {}
    high_score = load()

    if name in high_score:
        if score > high_score.get(name):
            high_score[name] = score
    else:
        high_score[name] = score

    try:
        with open(PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(high_score.keys())
            writer.writerow(high_score.values())
    except Exception as e:
        print(f"Error updating: {e}")

def sort(high_score: dict) -> dict:
    sorted_high_score = {k: v for k, v in sorted(high_score.items(), key=lambda item: item[1])}
    return sorted_high_score

#Eli
def display_score():
    raise NotImplementedError

# Use this to test your function
if __name__  == "__main__":
    update("John", 20)
    update("Anna", 80)
    update("John", 90)