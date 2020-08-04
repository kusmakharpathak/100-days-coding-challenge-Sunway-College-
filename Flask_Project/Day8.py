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

from flask import Flask, render_template, request
app = Flask(__name__)
SECRET_KEY = 'development key'
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        address = request.form['address']
        p_number = request.form['p_number']
        return f"My name is {f_name} {l_name}.<br>I live in {address}.<br>My contact details is {p_number}.<br>Thank You..."
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
