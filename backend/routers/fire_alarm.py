from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
import models

fire_alarm_router = APIRouter()

@fire_alarm_router.get("/fire-alarms/", tags=["fire_alarms"])
def read_fire_alarms(db: Session = Depends(get_db)):
    # Здесь будет логика для получения данных о датчиках пожарной сигнализации
    pass