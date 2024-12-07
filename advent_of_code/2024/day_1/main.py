from pathlib import Path

def sum_of_absolute_differences(list1:list, list2:list) -> int:
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")

    return sum(abs(x - y) for x, y in zip(list1, list2))

def calculate_similarity_score(list1:list, list2:list) -> int:
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    score = []
    for x in list1:
        if x not in list2:
            pass
        else:
            score.append(x * list2.count(x))

    return sum(score)

if __name__ == "__main__":
    # Calculate the sum of the absolute differences between the columns
    # Define the path to the input file
    input_file = Path("/Users/bradyspiva/Documents/Dev/advent_of_code/advent_of_code/2024/day_1/data/input.txt")

    # Initialize lists to store the columns
    column1 = []
    column2 = []

    # Read the file and load the columns into the lists
    with input_file.open() as file:
        for line in file:
            col1, col2 = line.strip().split()
            column1.append(int(col1))
            column2.append(int(col2))
    # sort the lists
    column1.sort()
    column2.sort()
    # result = sum_of_absolute_differences(column1, column2)
    result = calculate_similarity_score(column1, column2)
    print(f"Result: {result}")