from flask import Flask, render_template

app = Flask(__name__)

def load_data():
    with open("src/user.csv", "r") as file:
        users = []
        datas = file.read().splitlines()
        for data in datas:
            users.append(data.split(','))
        return users
    
@app.route('/')
def main():
    return render_template("main.html")

@app.route('/user')
def home():
    users = load_data()
    return render_template("index.html", users=users)

@app.route('/user/<user_id>')
def user_info(user_id):
    users = load_data()
    for user in users:
        if user[0] == user_id:
            return render_template("user_info.html", user=user)

if __name__ == "__main__":
    app.run(debug=True, port=8000)