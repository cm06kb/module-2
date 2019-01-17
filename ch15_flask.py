from flask import Flask
app = Flask("myApp")
@app.route("/")
def hello():
    print( "This is a index page")
    return "<h1>This is a index page</h1>"





@app.route("/bio")
def hello_bio():
    return "<h1>This is my bio page</h1>"


app.run(debug=True)