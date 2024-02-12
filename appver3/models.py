from flask_pymongo import pymongo
from flask_pymongo.wrappers import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client.tasks  # Replace 'tasks' with your actual database name

class Task:
    @staticmethod
    def add_task(title, description):
        try:
            result = db.tasks.insert_one({'title': title, 'description': description})
            return result.inserted_id
        except Exception as e:
            print(f"Error adding task: {e}")
            return None

    @staticmethod
    def get_all_tasks():
        try:
            return db.tasks.find()
        except Exception as e:
            print(f"Error fetching tasks: {e}")
            return None

    @staticmethod
    def delete_task(task_id):
        try:
            db.tasks.delete_one({'_id': ObjectId(task_id)})
        except Exception as e:
            print(f"Error deleting task: {e}")

    @staticmethod
    def get_task_by_id(task_id):
        try:
            return db.tasks.find_one({'_id': ObjectId(task_id)})
        except Exception as e:
            print(f"Error fetching task by ID: {e}")
            return None

    @staticmethod
    def update_task(task_id, title, description):
        try:
            db.tasks.update_one({'_id': ObjectId(task_id)}, {'$set': {'title': title, 'description': description}})
        except Exception as e:
            print(f"Error updating task: {e}")
