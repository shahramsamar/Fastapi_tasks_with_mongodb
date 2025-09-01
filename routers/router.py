from fastapi import APIRouter
from models.model import Tasks
from configurations.database import tasks_collection


MyRuter = APIRouter()




@MyRuter.get("/tasks")
async def get_tasks():
    tasks = list(tasks_collection.find({},{"_id":0}))  
    return {"tasks":tasks}  



@MyRuter.post("/add_task")
async def add_task(task:Tasks):
    task_data = task.dict()
    tasks_collection.insert_one(task_data)
    return {"message":"Task added successfully"}
