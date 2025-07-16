from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import SessionLocal

router = APIRouter(prefix='/projects', tags=['projects'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=schemas.ProjectRead)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    new_project = models.Project(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@router.get('/', response_model=list[schemas.ProjectRead])
def list_projects(language: str = '', db: Session = Depends(get_db)):
    query = db.query(models.Project)
    if language:
        query = query.filter(models.Project.language == language)
    return query.all()
