from fastapi import APIRouter, Depends
# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String

from database.database import get_db
import models

user_router = APIRouter()

status_to_color = {
    "Guest": "bg-blue-grey-lighten-3",
    "Employee": "bg-green-lighten-3",
    "Supervisor": "bg-orange-lighten-3",
    "Admin": "bg-red-lighten-3",
}

# Локации
class User():
    def __init__(self, name):
        self.name = name
        # self.description = description
        self.status = "Guest"  # Начальный статус
        self.color = "bg-blue-grey-lighten-3"
        self.img = ""

    def update_status(self, new_status):
        if new_status not in status_to_color:
            raise ValueError("Invalid status")
        else:
            new_color = status_to_color[new_status]
            self.status = new_status
            self.color = new_color

# Локации
users = {
    "1": User("Игорь"),
    "2": User("Миша"),
    "3": User("Слава"),
    "4": User("Даша"),
    "5": User("Маша"),
}

