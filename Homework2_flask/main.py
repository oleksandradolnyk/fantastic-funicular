import random, string
import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/password")
def generate_password():
    return ''.join(random.choices(string.digits + string.ascii_letters + string.punctuation, k=random.randint(10, 20)))

@app.route("/csv")
def calculate_average():
    data = pd.read_csv('data/hw.csv', sep=", ")
    height = data['Height(Inches)'].mean()
    weight = data['Weight(Pounds)'].mean()
    return f"Height: {height} Weight: {weight}"