from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.models.student import Student
from backend.schemas.student_schema import StudentCreate
from backend.app.dependencies import get_db

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = Student(
        user_id=student.user_id,
        department=student.department,
        current_gpa=student.current_gpa,
        interests=student.interests,
        career_goal=student.career_goal
    )

    db.add(new_student)
    db.commit()

    return {
        "message": "Student profile created"
    }


@router.get("/")
def get_students(
    db: Session = Depends(get_db)
):
    return db.query(Student).all()
@router.put("/{student_id}")
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    db_student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db_student.user_id = student.user_id
    db_student.department = student.department
    db_student.current_gpa = student.current_gpa
    db_student.interests = student.interests
    db_student.career_goal = student.career_goal

    db.commit()

    return {
        "message": "Student updated successfully"
    }

@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    db_student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(db_student)

    db.commit()

    return {
        "message": "Student deleted successfully"
    }