from flask import Flask

app = Flask(__name__)


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name="Kazuki Pickersgill"):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def display_conversion(celsius=0):
    return f"{celsius}C = {convert_celsius_to_fahrenheit(float(celsius))}F"


if __name__ == '__main__':
    app.run()
