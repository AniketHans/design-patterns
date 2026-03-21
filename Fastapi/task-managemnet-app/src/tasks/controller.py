from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

def createTask(body: TaskSchema, db: Session):
    data = body.model_dump()
    new_task = TaskModel(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"]
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task) # This will return the actual created row from the db
    return {"task": new_task}
    
def getTasks(db:Session):
    return db.query(TaskModel).all()

def getTaskById(task_id: int, db:Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task id does not exist")
    return task

def updateTaskById(updated_task: TaskSchema, task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    update_task_dict = updated_task.model_dump()
    
    for key, value in update_task_dict.items():
        setattr(task, key, value)
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return {"task":task}

def deleteTaskById(task_id: int, db:Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
         raise HTTPException(status_code=404, detail="Task id does not exist")
    db.delete(task)
    db.commit()
    return None