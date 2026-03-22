from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_router
from src.users.router import user_router

# Here, our application will try to connect DB first and if it is able to connect then it will create the tables
Base.metadata.create_all(engine)

app = FastAPI(title="A task management app")
app.include_router(task_router)
app.include_router(user_router)
