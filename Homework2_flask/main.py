import random, string
from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/password")
def generate_password():
    pswd = ''.join(random.choices(string.digits + string.ascii_letters + string.punctuation, k=random.randint(10, 20)))
    return pswd

@app.route("/csv")
def calculate_average():
    data = pd.read_csv('hw.csv', sep=", ")
    height = data['Height(Inches)'].mean()
    weight = data['Weight(Pounds)'].mean()
    return f"Height: {height} Weight: {weight}"
    # Height: 67.99311359679999 Weight: 127.07942116080001