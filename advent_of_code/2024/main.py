# in case you want to run the whole thing at once
from day_3 import Day3
# ...import other day classes...

def main():
    days = [Day3(), 
            # ...instantiate other day classes...
    ]

    for day in days:
        day.load_data()
        result = day.solve()
        print(f"Day {day.day} Result: {result}")

if __name__ == "__main__":
    main()