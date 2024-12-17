
from pathlib import Path

class AdventDay:
    def __init__(self, day: int):
        self.day = day
        self.cwd = Path.cwd()
        self.input_file = self.cwd / "data" / f"day_{day}.txt"
        self.reports = []

    def load_data(self, process_line=lambda line: line.strip().split()):
        with self.input_file.open() as file:
            for line in file:
                processed_data = process_line(line)
                self.reports.append(processed_data)

    def solve(self):
        raise NotImplementedError("Subclasses should implement this method")