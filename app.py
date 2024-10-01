from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # This loads the index.html file

@app.route('/convert', methods=['POST'])
def convert_temperature():
    temp = float(request.form['temperature'])
    unit = request.form['unit']

    if unit == 'C':
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        result = f"Fahrenheit: {fahrenheit:.2f}, Kelvin: {kelvin:.2f}"
    elif unit == 'F':
        celsius = (temp - 32) * 5/9
        kelvin = (temp + 459.67) * 5/9
        result = f"Celsius: {celsius:.2f}, Kelvin: {kelvin:.2f}"
    elif unit == 'K':
        celsius = temp - 273.15
        fahrenheit = (temp * 9/5) - 459.67
        result = f"Celsius: {celsius:.2f}, Fahrenheit: {fahrenheit:.2f}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
