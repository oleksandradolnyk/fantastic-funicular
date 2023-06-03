import csv, random, string
from http import HTTPStatus

import pandas as pd
import requests

from faker import Faker
from flask import Flask, Response, request
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

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
            password = "".join(random.choices(string.ascii_lowercase +
                                              string.ascii_uppercase +
                                              string.digits +
                                              string.punctuation,
                                              k=random.randint(15, 30)))
            year = random.randint(1963, 2005)
            month = random.randint(1, 12)
            if month == 2:
                max_days = 28
            elif month in [4, 6, 9, 11]:
                max_days = 30
            else:
                max_days = 31
            day = random.randint(1, max_days)
            birthday = '{day}/{month}/{year}'.format(day=day, month=month, year=year)
            writer.writerow({
                "first_name": faker_instance.first_name(),
                "last_name": faker_instance.last_name(),
                "email": faker_instance.ascii_free_email(),
                "password": password,
                "birthday": birthday
                })
    data = pd.read_csv("data/students.csv")
    return data.to_html()

@app.route("/bitcoin_rate")
@use_kwargs(
    {
        "currency": fields.Str(
            load_default="USD"
        ),
        "convert": fields.Int(
            load_default=100
        )
    },
    location="query"
)
def get_bitcoin_value(currency, convert):
    rates_result = requests.get(url="https://bitpay.com/api/rates").json()
    symbols_result = requests.get(url="https://bitpay.com/currencies").json()
    for entity in rates_result:
        if entity['code'] == currency:
            rate = entity['rate']
    for entity in symbols_result['data']:
        if entity['code'] == currency:
            currency_symbol = entity['symbol']
    return f'Value of {convert} BTC is {convert*rate} {currency_symbol} ({currency})'

app.run(port=5001, debug=True)
