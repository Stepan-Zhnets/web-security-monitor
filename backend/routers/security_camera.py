from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from database.database import get_db
import models

security_camera_router = APIRouter()


class Camera():
    def __init__(self, name, ip, description):
        self.name = name
        self.ip = ip
        self.description = description
        self.status = "None"  # Начальный статус
        self.img = ''

    def update_status(self, new_status):
        self.status = new_status

security_cameras = {
    "1": Camera("Отдел-Продаж", "172.16.0.1", "Description of Camera 1"),
    "2": Camera("Отдел-1С", "172.16.0.2", "Description of Camera 2"),
    "3": Camera("Отдел-Кадров", "172.16.0.3", "Description of Camera 3"),
    "4": Camera("Отдел-IT", "172.16.0.4", "Description of Camera 4"),
    "5": Camera("Склад-IT", "172.16.0.5", "Description of Camera 5"),
}