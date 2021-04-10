from flask import Flask, jsonify
from flask import request
import json
# decoded_object = json.loads(original_string)
app = Flask(__name__)


todos = [{ "label": "Sample", "done": True}]

# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return '<h1>Hello!</h1>'

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)