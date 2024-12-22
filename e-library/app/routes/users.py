from fastapi import APIRouter, HTTPException
from app.models import User
from app.database import users, user_id_num

user_router = APIRouter()
@user_router.post("/")
def user_create(user: User):
    global user_id_num
    user.id = user_id_num
    users[user_id_num] = user
    user_id_num += 1
    return user

@user_router.get("/")
def users_list():
    return list(users.values())

@user_router.get("/{user_id}")
def get_user(user_id: int):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/{user_id}")
def update_user(user_id: int, updated_user: User):
   user = users.get(user_id)
   if not user:
      raise HTTPException(status_code=404, detail="User not found")
   updated_user.id = user
   return updated_user

@user_router.patch("/{user_id}/deactivate")
def deactivate_user(user_id: int):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_deactivate = user.copy(update={"is_active": False})
    users[user_id] = user_deactivate
    return {"message": f"User {user_id} deactivated"}   


