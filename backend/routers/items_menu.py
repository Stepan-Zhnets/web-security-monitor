from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from database.database import get_db
import models

items_menu_router = APIRouter()

class Item():
    def __init__(self, name, link, color):
        self.name = name
        self.link = link
        self.color = color

items_menu = {
    "1": Item("surveillance cameras", "/security", "green"),
    "2": Item("locations monitor", "/locations_monitor", "orange"),
    "3": Item("informations", "/info", "blue"),
    "4": Item("users list", "/users", "lime")
}
