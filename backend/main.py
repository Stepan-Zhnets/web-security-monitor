from fastapi import(
    FastAPI,
    HTTPException,
    )
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from pydantic import BaseModel
import asyncio
# Database
from database.database import(
    engine,
    Base,
    SessionLocal
    )
# Routers
from routers import(
    items_menu_router,
    location_router,
    security_camera_router,
    fire_alarm_router,
    user_router
    )

#Объекты
from routers.items_menu import items_menu
from routers.location import locations
from routers.security_camera import security_cameras
from routers.user import users

app = FastAPI()

# Настройка CORS
origins = [
    "http://localhost:3000",
    "hhtp://127.0.0.1:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(items_menu_router)
app.include_router(location_router)
app.include_router(security_camera_router)
# app.fire_alarm_router(fire_alarm_router)
app.include_router(user_router)

@app.get("/api/items_menu", tags=["items"])
async def get_items_menu():
    return items_menu

# Локации
@app.get("/api/locations", tags=["locations"])
async def get_locations():
    return locations

# Запись в БД о новых локациях
@app.put("/locations/{location_id}/update-status", tags=["locations"])
async def update_location_status(location_id: str, new_status: str):
    if location_id not in locations:
        raise HTTPException(status_code=404, detail="Location not found")
    try:
        locations[location_id].update_status(new_status)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Status updated"}

# Камеры
@app.get("/api/security_cameras", tags=["security_cameras"])
async def get_camera():
    return security_cameras

# Датчики пажара
@app.get("/api/fire_alarm", tags=["fire_alarms"])
async def get_fire_alarm():
    pass

# Пользователи
@app.get("/api/users", tags=["users"])
async def get_users():
    return users

# main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)