from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_router


# Here, our application will try to connect DB first and if it is able to connect then it will create the tables
Base.metadata.create_all(engine)

app = FastAPI(title="A task management app")
app.include_router(task_router)
