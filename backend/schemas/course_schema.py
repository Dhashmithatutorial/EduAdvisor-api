from pydantic import BaseModel


class CourseCreate(BaseModel):
    course_name: str
    credits: int
    category: str
    prerequisite: str | None = None