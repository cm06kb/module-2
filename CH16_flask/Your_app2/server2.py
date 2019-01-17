from flask import Flask, render_template,  request
import sys

#app = Flask("myApp")
#@app.route("/")
#def index_page():
#    return render_template("server.html")
app = Flask("myApp")
@app.route("/")
def index():
    return render_template("server.html")

@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    print(form_data)
    email = form_data["email"]
    name=form_data["name"]
    return render_template("confirmation.html", title="Form confirmation", **locals()) 

@app.route("/about")
def about():
   	return render_template("about.html", title="about") 
#
#@app.route("/")
#def business_news():
#    return "<h1>This is business news homepage</h1>"


#@app.route("/business/eurozone")
#def business_news_eurozone():
#    return "<h1>This is business news relating to the eurozone</h1>"
#
#@app.route("/world")
#def world_news():
#    title = "<h1>This is world news home</h1>"
#    return title





app.run(debug=True)
