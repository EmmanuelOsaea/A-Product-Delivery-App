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

@validator('discord_id')
def validate_discord_id(cls, s):
  if s is None:
    return s
    # Validation Sample: Discord username#12345 format
if '#' not in s or len(s.split('#') [1]) != 5:
   raise ValueError('Discord ID format undetected, expected username#12345')
  return s

def send_email(email: str, message: str):
  # Email sending logic here
print(f"Sending email to {email}: {message}")

def send_discord_message(discord_id: str, message: str):
  # Discord sending logic here
  print(f"Sending Discord message to {discord_id}: {message}")

def send_push_notification(tokens: List[str], message: str):
  for token in tokens
  print(f"Sending push notification to {token}: {message}")

@app.post("/notify/")
async def send_notification(notification: Notification, background_tasks: BackgroundTasks): 
if notification.email:
  background_tasks.add_task(send_email, notification.discord_id, notification.message)
if notification.discord_id:
  background_tasks.add_task(send_discord_message, notification.discord_id, notification.message)
app.get("/health")
async def health_check():
  return {"status": "Notification service is active"}
