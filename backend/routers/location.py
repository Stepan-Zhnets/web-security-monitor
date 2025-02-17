from fastapi import APIRouter, Depends
# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String

from database.database import get_db
import models

location_router = APIRouter()

status_to_color = {
    "Normal": "bg-green-lighten-3",
    "Warning": "bg-orange-lighten-3",
    "Critical": "bg-red-lighten-3",
}

# Локации
class Location():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.status = "Normal"  # Начальный статус
        self.color = "bg-green-lighten-3"

    def update_status(self, new_status):
        if new_status not in status_to_color:
            raise ValueError("Invalid status")
        else:
            new_color = status_to_color[new_status]
            self.status = new_status
            self.color = new_color

# Локации
locations = {
    "1": Location("Отдел-Продаж", "Description of Location 1"),
    "2": Location("Отдел-1С", "Description of Location 2"),
    "3": Location("Отдел-Кадров", "Description of Location 3"),
    "4": Location("Отдел-IT", "Description of Location 4"),
    "5": Location("Склад-IT", "Description of Location 5"),
}