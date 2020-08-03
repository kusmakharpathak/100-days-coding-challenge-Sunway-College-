"""
Author :   Kusmakhar Pathak
Created:   3 August 2020
(c) Copyright by Kusmakhar Pathak.
"""
# Web programming using Python flask

"""
    Welcome to restful API with Flask and MongoDB.
    This Exercises will go for 3 weeks to build a complete restful API and blogging site.
    In this section I will demonstrate you to how to create WTForms, template rendering, Data base connection,
    form validation and static file rendering like images, css, js. 
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to restful API with Flask and MongoDB."

if __name__ == "__main__":
    app.run(debug=True)
