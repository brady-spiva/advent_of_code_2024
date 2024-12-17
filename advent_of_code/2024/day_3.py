
import re
from advent_day import AdventDay
import pprint


class DayX(AdventDay):
    def __init__(self, day: int):
        super().__init__(day=day)

    def solve(self):
        # Implement the solution for day X
        # Regex to match 'mul' with two 1-3 digit numbers
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        # pprint.pprint(self.reports)
        matches = []

        # Extract all matches
        for report in self.reports:
            for string in report:
                match = re.findall(pattern, string)
                matches.extend(match)
        
        # Convert to a list of lists with integers
        # multiply the two numbers and add the result to a list
        multiplied_pairs = [int(a) * int(b) for a, b in matches]

        # sum all of the results
        result = sum(multiplied_pairs)
        return result

if __name__ == "__main__":
    day = DayX(day=3)  # Replace X with the actual day number
    day.load_data()
    result = day.solve()
    print(f"Result: {result}")