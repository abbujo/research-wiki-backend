from flask import request, jsonify, Flask
from pymongo import MongoClient
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


client = MongoClient(
    "mongodb+srv://abbu93:itsmeabbu20@cluster0.bafsc.mongodb.net/TestPyMongo?retryWrites=true&w=majority")
client.list_database_names()
db = client["TestPyMongo"]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Research Wiki Archive</h1><p>This site is a prototype API for Research Wiki.</p>"

@app.route('/api/v1/query', methods=['GET'])
def api_query1():
    if 'label' in request.args:
        label = request.args['label']
    else:
        return "Error: No label field provided. Please specify a label."

    collection_name = "query"
    collection = db[collection_name]
    data = collection.find({"label": label})
    # Create an empty list for our results
    results = []
    for x in data:
        print(x["res"])
        results.append(x["res"])

    response =jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# To perform a search
# /api/v1/resources?label=Abhishek
@app.route('/api/v1/resources', methods=['GET'])
def api_label():
    # Check if an Label was provided as part of the URL.
    # If Label is provided, assign it to a variable.
    # If no Label is provided, display an error in the browser.
    if 'label' in request.args:
        label = request.args['label']
    else:
        return "Error: No label field provided. Please specify a label."

    collection_name = "test"
    collection = db[collection_name]
    data = collection.find({"label": label})
    # Create an empty list for our results
    results = []
    for x in data:
      
      results.append(x)

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    response =jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)