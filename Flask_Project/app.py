"""
Author :   Kusmakhar Pathak
(c) Copyright by Kusmakhar Pathak.
"""
# Web programming using Python flask

"""
    Welcome to restful API with Flask and MongoDB.
    This Exercises will go for 3 weeks to build a complete restful API and blogging site.
    In this section I will demonstrate you to how to create WTForms, templates rendering, Data base connection,
    form validation and static file rendering like images, css, js. 
    Templates and form rendering
"""

from flask import Flask, render_template
import json
app = Flask(__name__)
SECRET_KEY = 'development key'
@app.route('/', methods=['POST', 'GET'])
def index():
    file = open('data.json')
    data = json.load(file)
    return render_template("index.html", data=(data['emp_details']))

if __name__ == "__main__":
    app.run(debug=True)
