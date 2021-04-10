from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [{ "label": "Sample", "done": True }]

# @app.route('/todos', methods=['GET'])
# # def hello_world():
# #     return '<h1>Hello!</h1>'

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    request.data = json.loads(request_body)
    json_text = jsonify(todos)
    return json_text


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)