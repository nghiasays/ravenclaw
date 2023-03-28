import conf
import logging

from fastapi import APIRouter

router = APIRouter()

logger = logging.getLogger()

@router.get("/users")
async def read_users():
    # Return all users
    logger.info("In read_users")
    pass

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    # Return a specific user by ID
    pass

@router.post("/users")
async def create_user():
    # Create a new user
    pass

@router.put("/users/{user_id}")
async def update_user(user_id: int):
    # Update a specific user by ID
    pass

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # Delete a specific user by ID
    pass