from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    name: str
    stack: str

class ProfileResponse(BaseModel):
    status: str
    user: User
    timestamp: str
    fact: str
    