from fastapi import FastApi, HTTPException, BackgroundTasks
from pydantic import BaseModel, EmailStr
from typing import List
from pydantic import BaseModel, validator
from typing import Optional

app = FastAPI(title="Notification Service")

# --- Schemas ---
class Notification(BaseModel):
  user_id: int
  message: str
  email: Optional[EmailStr] = None
  discord_id: Optional[str] = None

@validator(
