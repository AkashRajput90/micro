from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from flask_caching import Cache
from models import Task
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')

class Config:
    MONGO_URI = "mongodb+srv://manhasakash990:Thakur123@tasks.sdxilnc.mongodb.net/?retryWrites=true&w=majority"
    CACHE_TYPE = 'simple'
    CACHE_TIMEOUT = 60

# Configure Flask app
app.config.from_object(Config)

# Initialize PyMongo and Flask-Cachinggd
mongo = PyMongo(app)
cache = Cache(app)

try:
    client = MongoClient(Config.MONGO_URI)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


@app.route('/')
def index():
    # Fetch tasks from the database every time the route is accessed
    tasks = Task.get_all_tasks()
    return render_template('index.html', tasks=tasks)


# Add task route
@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        Task.add_task(title, description)
        return redirect(url_for('index'))
    return render_template('add_task.html')

# Delete task route
@app.route('/delete_task/<ObjectId:task_id>')
def delete_task(task_id):
    Task.delete_task(task_id)
    return redirect(url_for('index'))

# Edit task route
@app.route('/edit_task/<ObjectId:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task_to_edit = Task.get_task_by_id(task_id)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        Task.update_task(task_id, title, description)
        return redirect(url_for('index'))
    return render_template('edit_task.html', task=task_to_edit)

# ... existing code ...

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
