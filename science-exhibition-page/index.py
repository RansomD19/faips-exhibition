from flask import Flask, render_template
import pandas as pd


data = pd.read_csv('data2.csv')
team_names = data['Team Name']
team_members = data['Team Members']
descs = data['Project Description']
img = data['Image']
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Opening page </h1>'


@app.route('/user/<id>')
def user(id):
    id = int(id)
    team_name = team_names[id-1]
    team_member = team_members[id-1]
    desc = descs[id-1]
    image = img[id-1]  

    return render_template('index.html', team_name = team_name, team_member = team_member, desc = desc, image=image)

#127.0.0.1:5000/user/Jasim
 
if __name__ == '__main__':
    app.run(debug=True)
