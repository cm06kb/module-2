from flask import Flask, render_template

#app = Flask("myApp")
#@app.route("/")
#def index_page():
#    return render_template("server.html")
app = Flask("myApp")
@app.route("/<name>")
def index_page(name):
    return render_template("server.html", name = name.title())



@app.route("/")
def business_news():
    return "<h1>This is business news homepage</h1>"


#@app.route("/business/eurozone")
#def business_news_eurozone():
#    return "<h1>This is business news relating to the eurozone</h1>"
#
#@app.route("/world")
#def world_news():
#    title = "<h1>This is world news home</h1>"
#    return title


app.run(debug=True)
