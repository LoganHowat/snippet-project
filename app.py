from flask import Flask, request
from seedData import seedData
import json

app = Flask(__name__)

@app.get('/snippets')
def get_all_snippets():
    return seedData

@app.get('/snippets/<id>')
def get_snippet_by_id(id):
    for snippet in seedData:
        if snippet["id"] == int(id):
            return snippet
    return 'No snippet found', 404

@app.post('/snippets')
def add_snippet():
    request_data = json.loads(request.data.decode('utf-8'))
    request_data["id"] = len(seedData) + 1
    seedData.append(request_data)
    return (seedData)