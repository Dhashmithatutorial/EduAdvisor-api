from pydantic import BaseModel


class StudentCreate(BaseModel):

    user_id: int

    department: str

    current_gpa: float

    interests: str

    career_goal: str