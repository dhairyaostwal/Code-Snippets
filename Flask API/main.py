from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Yash Rao 😎'

# app function
# enter the link ('/num1+num2')

@app.route('/sum/<string:a>/<string:b>')
def sum(a,b):
    a = int(a)
    b = int(b)
    ans = a + b
    result = {
        "Num1": a,
        "Num2" : b,
        "Sum": ans
    }
    return jsonify(result)

@app.route('/product/<string:a>/<string:b>')
def product(a,b):
    a = int(a)
    b = int(b)
    ans = a * b
    result = {
        "Num1": a,
        "Num2" : b,
        "Product": ans
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
