import csv

#  Create file if not exists
def check_file():
    try:
        with open("high_score.csv", "x"):
            return
        with open("user.csv", "x"):
            return
    except FileExistsError:
        return
    
def write(path: str, data: dict) -> None:
    try:
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data.keys())
            writer.writerow(data.values())
    except Exception as e:
        print(f"Error updating: {e}")
    
# Load csv as dictionary
def load(path: str, integer: bool = False) -> dict:
    data = {}
    my_list = []
    try:
        with open(path, newline="") as file:
            reader = csv.reader(file, delimiter=",")
            if reader is None:
                return data
            for row in reader:
                my_list.append(row)
            if len(my_list) != 2:
                return data
            for key, value in zip(my_list[0], my_list[1]):
                if integer:
                    data[key] = int(value)
                else:
                    data[key] = value 
    except Exception as e:
        print(f"Error loading: {e}")

    return data