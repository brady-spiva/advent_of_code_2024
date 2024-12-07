from pathlib import Path

def determine_safety_of_nuclear_reactor_report(report:list) -> bool:
    
    # what are the differences between the levels?
    differences = [y - x for x, y in zip(report, report[1:])]
    
    # safe levels have an absolute difference between 1 and 3
    if all([1 <= abs(diff) <= 3 for diff in differences]):
        # are the differences all increasing or decreasing?
        if all([diff >= 0 for diff in differences]) or all([diff <= 0 for diff in differences]):
            return True
    return False

if __name__ == "__main__":
    # Get the current working directory
    cwd = Path.cwd()

    # Construct a relative path to a file
    input_file = cwd / "data" / "reports.txt"

    # Initialize lists to store the columns
    reports = []

    # Read the file and load the columns into the lists
    with input_file.open() as file:
        for line in file:
            data = line.strip().split()
            data = list(map(int, data))
            reports.append(data)
    result = sum([determine_safety_of_nuclear_reactor_report(report) for report in reports])
    print(f"Result: {result}")