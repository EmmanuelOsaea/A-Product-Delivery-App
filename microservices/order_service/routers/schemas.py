from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List

class NotificationBase(BaseModel):
    user_id: int
    message: str
  
class NotificationCreate(NotificationBase);
    email: Optional[EmailStr] = None
    discord_id: Optional[str] = None
    push_tokens: Optional[List[str]] = []

   @validator('discord-id')
def validate_discord_id(cls, s):
  if s is None:
     return s
    # Validate Discord username#12345 format
    if '#' not in s or len(s.split('#') [1] != 5:
         raise ValueError('Discord ID format undetected, expected username#12345')
      return s

class NotificationResponse(NotificationBase):
  
