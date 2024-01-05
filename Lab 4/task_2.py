import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)

    data_products = [item["score"] * item["weight"] for item in data]

    return round(sum(data_products), 3)

print(task())
