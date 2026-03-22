from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from typing import List
from src.utils.helpers import is_auth
from src.users.models import UserModel


task_router = APIRouter(prefix="/tasks")


@task_router.post("/create", response_model= TaskResponseSchema ,status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db: Session = Depends(get_db), user: UserModel = Depends(is_auth)):
    return controller.createTask(body, db, user)

@task_router.get("/", response_model= List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session = Depends(get_db), user: UserModel = Depends(is_auth)):
    return controller.getTasks(db, user)

@task_router.get("/{task_id}", response_model= TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_task_by_id(task_id:int, db: Session = Depends(get_db), user: UserModel = Depends(is_auth)):
    return controller.getTaskById(task_id, db, user)

@task_router.put("/{task_id}/update", response_model= TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def update_task_by_id(task_id: int, body: TaskSchema, db: Session = Depends(get_db), user: UserModel = Depends(is_auth)):
    return controller.updateTaskById(body, task_id, db, user)


@task_router.delete("/{task_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
def get_task_by_id(task_id:int, db: Session = Depends(get_db), user: UserModel = Depends(is_auth)):
    return controller.deleteTaskById(task_id, db, user)