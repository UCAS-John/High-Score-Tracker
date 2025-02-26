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

    high_score = sort_dict(high_score)
    try:
        with open(PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(high_score.keys())
            writer.writerow(high_score.values())
    except Exception as e:
        print(f"Error updating: {e}")

def sort_dict(high_score: dict) -> dict:
    sorted_high_score = {k: v for k, v in sorted(high_score.items(), key=lambda item: item[1], reverse=True)}
    return sorted_high_score

#Eli
def display_top_ten() -> None:
    scores = {}
    scores = load()
    if not scores:
        print("There is no high score yet!")
        return
    
    top = {k: v for i, (k, v) in enumerate(scores.items()) if i < 10} 

    scores = sort_dict(scores)
    for name, score in top.items():
        print(f"{name}: {score}")

# Use this to test your function
if __name__  == "__main__":
    display_top_ten()