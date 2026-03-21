from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from typing import List


task_router = APIRouter(prefix="/tasks")


@task_router.post("/create", response_model= TaskResponseSchema ,status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.createTask(body, db)

@task_router.get("/", response_model= List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session = Depends(get_db)):
    return controller.getTasks(db)

@task_router.get("/{task_id}", response_model= TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_task_by_id(task_id:int, db: Session = Depends(get_db)):
    return controller.getTaskById(task_id, db)

@task_router.put("/{task_id}/update", response_model= TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def update_task_by_id(task_id: int, body: TaskSchema, db: Session = Depends(get_db)):
    return controller.updateTaskById(body, task_id, db)


@task_router.delete("/{task_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
def get_task_by_id(task_id:int, db: Session = Depends(get_db)):
    return controller.deleteTaskById(task_id, db)