from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def home():
    users = [
        {'name': 'Alice', 'age': 25, 'phone': '123-456-7890'},
        {'name': 'Bob', 'age': 30, 'phone': '987-654-3210'},
        {'name': 'Charlie', 'age': 35, 'phone': '555-123-4567'}
    ]
    response = render_template("index2.html", username=users)
    return response

if __name__ == "__main__":
    app.run(debug=True, port=8000)