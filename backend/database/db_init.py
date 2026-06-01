from backend.database.connection import engine

from backend.models.user import User
from backend.models.course import Course
from backend.models.student import Student
from backend.models.student_course import StudentCourse

def create_tables():
    User.metadata.create_all(bind=engine)
    Course.metadata.create_all(bind=engine)
    Student.metadata.create_all(bind=engine)
    StudentCourse.metadata.create_all(bind=engine)