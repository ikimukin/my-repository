from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return(render_template("index.html", number1=10, number2=20))

@app.route("/<string:num1>/<string:num2>")
def numbers(num1, num2):
    return(render_template("index.html", number1=num1, number2=num2))

@app.route("/sum/<string:first>/<string:second>")
def sum(first, second):
    if first.isdigit() and second.isdigit:
        mysum = int(first) + int(second)
        return(render_template("body.html", value1=first, value2=second, sum=mysum))
    else:
        return("poor URL")
        


if __name__== "__main__":
    app.run(debug=False, port=5000)
    # app.run(host= '0.0.0.0', port=8081)
