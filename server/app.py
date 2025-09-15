from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Print route
@app.route('/print/<string:word>')
def print_string(word):
    print(word)      # prints to console
    return word      # return plain text only

# Count route
@app.route('/count/<int:number>')
def count(number):
    # Add trailing newline to match test expectation
    numbers = "\n".join(str(n) for n in range(number)) + "\n"
    return numbers

# Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else "Infinity"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Operation not supported"

    return str(result)  # return just the result as text
