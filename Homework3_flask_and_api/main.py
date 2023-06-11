import csv, requests

from faker import Faker

from flask import Flask

from webargs import fields, validate
from webargs.flaskparser import use_kwargs

app = Flask(__name__)

fake = Faker("uk_UA")

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!!</p>"

@app.route("/students")
@use_kwargs(
    {
        "number": fields.Int(
            load_default=10, validate=validate.Range(1, 1000)
        ),
    },
    location="query"
)
def generate_students(number):
    headers = ["first_name", "last_name", "email", "password", "birthday"]
    data = []
    with open('data/students.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for student in range(number):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.ascii_free_email()
            password = fake.password(length=25)
            birthday = fake.date_of_birth(minimum_age=18, maximum_age=65)
            person = {"first_name": first_name,
                      "last_name": last_name,
                      "email": email,
                      "password": password,
                      "birthday": birthday}
            data.append(person)
        writer.writerows(data)
    return data

@app.route("/bitcoin_rate")
@use_kwargs(
    {
        "currency": fields.Str(
            load_default="USD"
        ),
        "convert": fields.Int(
            load_default=100, validate=validate.Range(min=1)
        )
    },
    location="query"
)
def get_bitcoin_value(currency, convert):
    rates_result = requests.get(url=f"https://bitpay.com/api/rates/{currency}").json()
    symbols_result = requests.get(url="https://bitpay.com/currencies").json()
    rate = rates_result['rate']
    for entity in symbols_result['data']:
        if entity['code'] == currency:
            currency_symbol = entity['symbol']
    return f'Value of {convert} BTC is {convert*rate} {currency_symbol} ({currency})'

if __name__ == '__main__':
    app.run(port=5001, debug=True)
