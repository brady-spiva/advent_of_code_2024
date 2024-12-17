from pathlib import Path

def determine_safety_of_nuclear_reactor_report(report:list) -> bool:
    
    def calculate_differences(report:list) -> list:
        return [y - x for x, y in zip(report, report[1:])]
    # what are the differences between the levels?
    differences = calculate_differences(report)
    
    # safe levels have an absolute difference between 1 and 3
    differences_bool = [1 <= abs(diff) <= 3 for diff in differences]

    if all(differences_bool):
        # are the differences all increasing or decreasing?
        if all([diff >= 0 for diff in differences]) or all([diff <= 0 for diff in differences]):
            return True
    else:
        # level 2 - include the problem dampener. Can we remove a single level from the report to make it safe?
        # try removing a single level
        for i, diff in enumerate(differences):
            if 1 <= abs(diff) <= 3:
                new_report = report[:i] + report[i+1:]
                if determine_safety_of_nuclear_reactor_report(new_report):
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