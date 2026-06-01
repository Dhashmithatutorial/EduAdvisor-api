from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from backend.database.connection import Base


class StudentCourse(Base):
    __tablename__ = "student_courses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.id")
    )