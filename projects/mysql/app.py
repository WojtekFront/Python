from flask import Flask, render_template

from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

Jobs = [
    {"id": 1,
     "title": "Python Development",
     "description": "This is a development application for Python development",
     "date": "2024-03-01",
     "time": "12:00:00",
     "location": "Warszawa",
     "salary": 10000

    },
    {"id": 2,
     "title": "Data Analyst",
     "description": "This is a development application for Analitic development",
     "date": "2024-01-01",
     "time": "12:00:00",
     "location": "Szczecin",
     "salary": 9000},
    {"id": 3,
     "title": "Support",
     "description": "This is a development application for  support",
     "date": "2024-03-03",
     "time": "12:00:00",
     "location": "Gdańsk",
    #  "salary": 
     },
    {"id": 4,
     "title": "Project manager",
     "description": "This is a development application for project menager",
     "date": "2024-02-01",
     "time": "12:00:00",
     "location": "Szczecin",
     "salary": 7000}

]


@app.route("/")
def hello_html():
    return render_template('home.html', 
                           jobs =Jobs)

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route("/p/")
def products():
    return "<p>Products</p><ol><li>Product 1</li><li>Product 2</li> <li>Product 3</li> <li>Product 4</li><li>Product 5</li> </ol>"

if __name__ == "__main__":
    app.run(debug=True)

   
