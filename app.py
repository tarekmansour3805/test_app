from flask import Flask, jsonify
from datetime import datetime, date

app = Flask(__name__)

@app.route("/")
def home():
	return "hello world"

@app.route("/age/<born>")
def calculate_age(born):
    
	born = datetime.strptime(born, "%m-%d-%Y")
	today = date.today()
	age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
	return jsonify({"age": age})

if __name__ == "__main__":
	app.run()