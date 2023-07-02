from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

CORS(app)

_tasks = []

@app.route("/tasks", methods=['GET', 'POST'])
def tasks():
  if request.method == 'GET':
    return jsonify({
      'tasks': _tasks,
    })

  else:
    post_data = request.get_json()
    _tasks.insert(0, {
      'taskID': uuid.uuid4().hex,
      'taskText': post_data.get('taskText')
    })
    return "Task added successfully"

@app.route("/tasks/<task_id>")
def remove_task(task_id):
  for task in _tasks:
    if task['taskID'] == task_id:
      _tasks.remove(task)
      return True
  
  return False
  

if __name__ == "__main__":
  app.run(debug=True)