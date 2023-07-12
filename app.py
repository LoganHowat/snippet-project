from flask import Flask, request
from flask_bcrypt import Bcrypt
from seedData import seedData
import json

app = Flask(__name__)

bcrypt = Bcrypt(app)

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

@app.post('/encrypt')
def hash_password():
    request_data = json.loads(request.data)
    hashed_password = bcrypt.generate_password_hash(request_data["password"], 18)
    return (hashed_password)

@app.post('/decrypt')
def test_hash_and_password():
    request_data = json.loads(request.data)
    is_valid = bcrypt.check_password_hash(request_data["hash"], request_data["password"])
    return ({"match": is_valid})

# Pass the data in form {hash: asdjfbasjdfhs, password: password}