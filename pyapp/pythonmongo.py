#This script Worked and Insluded in the Image!

from flask import Flask, render_template, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# 3T: Aug.7-23: chaning the localhost with 'mongodb', to see if python app can work
# client = MongoClient('mongodb://admin:adminroot@localhost:27017/')

client = MongoClient('mongodb://admin:adminroot@mongodb:27017/')


db = client['user-accounts']
collection = db['users']

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Retrieving form data
        name = request.form['name']
        email = request.form['email']
        age = int (request.form['age'])

        # Suggested to create dictionay with the form data
        document = {
            'name': name,
            'email': email,
            'age': age
        }


        # Insert the record into the database
        collection.insert_one(document)

        # Redirect to success page or render a template
        return 'User added successfully!'

    # Rendering the form template for GET requests

    return render_template('form.html')

if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)
