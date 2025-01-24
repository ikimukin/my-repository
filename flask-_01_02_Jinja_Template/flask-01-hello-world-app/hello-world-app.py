from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return("Hello World, Love from ibrahim")

@app.route("/bye")
def goodbye():
    return("Goodbye, to you all")

@app.route("/third/subthird")
def third():
    return("This is a double path")


@app.route("/fourth/<string:id>")
def fourth(id):
    output = f"Your ID is {id}"
    return(output)


if __name__ == '__main__':

    app.run(debug=False, port=5000)
    # app.run(host= '0.0.0.0', port=8081)
