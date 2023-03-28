import conf
import logging

from fastapi import APIRouter

app = APIRouter()

logger = logging.getLogger()

@app.get("/users")
async def read_users():
    # Return all users
    logger.info("In read_users")
    pass

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    # Return a specific user by ID
    pass

@app.post("/users")
async def create_user():
    # Create a new user
    pass

@app.put("/users/{user_id}")
async def update_user(user_id: int):
    # Update a specific user by ID
    pass

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # Delete a specific user by ID
    pass