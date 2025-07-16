from fastapi import FastAPI
from .routers import users, projects, messages
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Together')

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(messages.router)

@app.get('/')
def read_root():
    return {'message': 'Together API'}
