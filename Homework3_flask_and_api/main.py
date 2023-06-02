import csv, random, string
import pandas as pd

from faker import Faker
from flask import Flask

app = Flask(__name__)

faker_instance = Faker("uk_UA")

@app.route("/")
def hello_world():
    # view
    return "<p>Hello, World!!!!</p>"

@app.route("/students/<int:counter>/")
def generate_students(counter):
    if not 0 <= counter <= 1000:
        return "ERROR: should be in range [1, 1000]"
    headers = ["first_name", "last_name", "email", "password", "birthday"]
    with open('data/students.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for student in range(counter):
            password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=random.randint(15, 30)))
            birthday = '{day}/{month}/{year}'.format(day=random.randint(1, 28), month=random.randint(1, 12), year=random.randint(1963, 2005))
            writer.writerow({
                "first_name": faker_instance.first_name(),
                "last_name": faker_instance.last_name(),
                "email": faker_instance.ascii_free_email(),
                "password": password,
                "birthday": birthday
                })
    data = pd.read_csv("data/students.csv")
    return data.to_html()

def get_bitcoin_value():
    # https://bitpay.com/api/rates
    # /bitcoin_rate?currency=UAH&convert=100
    # input parameter currency code
    # default is USD
    # return value currency of bitcoin
    # * https://bitpay.com/api/
    # * return symbol of input currency code
    # * add one more input parameter count and multiply by currency (int)
    pass

app.run(port=5001, debug=True)

