from file import load, write

SCORE_PATH = "high_score.csv"

# Update high score if score is higher than previous score
def update(name: str, score: int) -> None:
    high_score = {}
    high_score = load(SCORE_PATH, integer=True)

    if name in high_score:
        if score > high_score[name]:
            high_score[name] = score
    else:
        high_score[name] = score

    high_score = sort_dict(high_score)

    write(SCORE_PATH, high_score)

# Sort Dictionary
def sort_dict(high_score: dict) -> dict:
    sorted_high_score = {k: v for k, v in sorted(high_score.items(), key=lambda item: item[1], reverse=True)}
    return sorted_high_score

# Display Top ten highest score
def display_top_ten() -> None:
    scores = {}
    scores = load(SCORE_PATH, integer=True)
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
    dictionary = {"JOhn" : 90,
                  "anna" : 80,
                  "h": 85,
                  "a": 85.5}
    print(dictionary)
    sorted_dict = sort_dict(dictionary)
    print(sorted_dict)