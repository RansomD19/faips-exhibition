from flask import Flask, render_template
import pandas as pd

#create a falsk instance
app = Flask(__name__)

#reading csv
data = pd.read_csv('data2.csv')
team_names = data['Team Name']
team_members = data['Team Members']
descs = data['Project Description']
img = data['Project Image']
app = Flask(__name__)

# create a route decorator
@app.route("/")

def index():
    return render_template("index.html")

@app.route("/content/<id>")
def content(id):
    id = int(id)
    team_name = team_names[id-1]
    team_member = team_members[id-1]
    desc = descs[id-1]
    image = img[id-1]  

    return render_template('content.html', team_name = team_name, team_member = team_member, desc = desc, image=image)

#create a custom error pages
#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
