from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import SessionLocal

router = APIRouter(prefix='/users', tags=['users'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail='Username already registered')
    new_user = models.User(username=user.username, password=user.password, bio=user.bio)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/', response_model=list[schemas.UserRead])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
