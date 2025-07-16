from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .. import models
from ..database import SessionLocal

router = APIRouter(prefix='/messages', tags=['messages'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class MessageCreate(BaseModel):
    sender_id: int
    receiver_id: int
    content: str

@router.post('/')
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    msg = models.Message(**message.dict())
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return {'status': 'sent'}
