from flask import Flask,jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print(request_body)
    
    todos.append(request_body)  # Agregar el contenido al final de la lista "todos"
    json_text = jsonify(todos)  # Convertir la lista actualizada a JSON
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        deleted_todo = todos.pop(position)
        return jsonify(deleted_todo)
    else:
        return "Position out of range"



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)