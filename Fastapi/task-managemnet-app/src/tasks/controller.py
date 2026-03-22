from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.users.models import UserModel

def createTask(body: TaskSchema, db: Session, user:UserModel):
    new_task = TaskModel(
        title = body.title,
        description = body.description,
        is_completed = body.is_completed,
        user_id = user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task) # This will return the actual created row from the db
    return new_task
    
def getTasks(db:Session, user: UserModel):
    return db.query(TaskModel).filter(TaskModel.user_id == user.id).all()

def getTaskById(task_id: int, db:Session, user: UserModel):
    task = db.query(TaskModel).filter(TaskModel.user_id == user.id).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task id does not exist")
    return task

def updateTaskById(updated_task: TaskSchema, task_id: int, db: Session, user: UserModel):
    task = db.query(TaskModel).filter(TaskModel.user_id == user.id).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task id does not exist")
        
    update_task_dict = updated_task.model_dump()
    
    for key, value in update_task_dict.items():
        setattr(task, key, value)
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task

def deleteTaskById(task_id: int, db:Session, user: UserModel):
    task = db.query(TaskModel).filter(TaskModel.user_id == user.id).filter(TaskModel.id == task_id).first()
    if not task:
         raise HTTPException(status_code=404, detail="Task id does not exist")
    db.delete(task)
    db.commit()
    return None