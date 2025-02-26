import csv

PATH = "high_score.csv"

# Create file if not exists
def check_file():
    try:
        with open(PATH, "x"):
            return
    except FileExistsError:
        return

# Load csv as dictionary
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
                high_score[key] = int(value) 
    except Exception as e:
        print(f"Error loading: {e}")

    return high_score

# Update high score if score is higher than previous score
def update(name: str, score: int) -> None:
    high_score = {}
    high_score = load()

    if name in high_score:
        if score > high_score[name]:
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

# Sort Dictionary
def sort_dict(high_score: dict) -> dict:
    sorted_high_score = {k: v for k, v in sorted(high_score.items(), key=lambda item: item[1], reverse=True)}
    return sorted_high_score

# Display Top ten highest score
def display_top_ten() -> None:
    scores = {}
    scores = load()
    if not scores:
        print("There is no high score yet!")
        return
    
    scores = sort_dict(scores)

    top = {k: v for i, (k, v) in enumerate(scores.items()) if i < 10} # Get top ten score in to dict

    print("\nTop ten highest score!")
    for name, score in top.items():
        print(f"{name}: {score}")
    print("")

# Use this to test your function
if __name__  == "__main__":
    display_top_ten()