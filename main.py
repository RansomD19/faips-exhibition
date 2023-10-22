from flask import Flask, render_template

#create a falsk instance
app = Flask(__name__)

# create a route decorator
@app.route("/")

def index():
    first_name = "John Doe"
    stuff = "This is <strong>Bold</strong>"
    fav = [1, 2, 3, 4, 4]
    return render_template("index.html", stuff=stuff, faviii=fav)

@app.route("/user/<name>")

def user(name):
    return render_template("user.html", name=name)


#create a custom error pages
#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
