import csv
import os


# def load_data():
#     with open("src/user.csv", "r") as file:
#         users = csv.DictReader(file)
#         return users

def home():
    with open("src/user.csv", "r") as file:
        users = csv.DictReader(file)
        for user in users:
            print(user)

home()

# if __name__ == "__main__":
#     current_dir = os.getcwd()
