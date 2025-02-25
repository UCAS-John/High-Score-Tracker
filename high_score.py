import csv

PATH = "high_score.csv"


# Locklin
def check_file():
    raise NotImplementedError

# John
def load():
    raise NotImplementedError

# John
def update():
    raise NotImplementedError

#Eli
def display_top_ten():
    scores = []
    with open("high_score.csv", "r") as file:
        for row in file:
            scores.append(row)
    top = 10
    for score in scores:
        if top <= 0:
            break
        print(score)
        top -= 1

# Use this to test your function
if __name__  == "__main__":
    pass