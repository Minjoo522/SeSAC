import csv

def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        user_list = []
        users = csv.DictReader(file, skipinitialspace=True)
        for user in users:
            user_list.append(user)
    return user_list


i_list = []
datas = load_file("src/user.csv")
for i in datas:
    i_list.append(i)
print(i_list)