import csv

def users():
    with open("./src/data_sapce.csv", "r", encoding="utf-8") as file:
        users = csv.DictReader(file)
        for row in users:
            print(row)


users()