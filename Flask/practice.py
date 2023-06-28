import csv

with open("./src/user.csv", "r") as file:
    users = csv.reader(file)
    for user in users:
        print(user)