import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
JSON_INDENT = 4


def task() -> None:
    with open(INPUT_FILENAME) as f:
        reader = csv.DictReader(f, delimiter=",", lineterminator="\n")
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(data, f, indent=JSON_INDENT)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
