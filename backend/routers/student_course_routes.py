from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.app.dependencies import get_db

from backend.models.student_course import (
    StudentCourse
)

from backend.schemas.student_course_schema import (
    StudentCourseCreate
)

router = APIRouter(
    prefix="/student-courses",
    tags=["Academic History"]
)


@router.post("/")
def add_completed_course(
    data: StudentCourseCreate,
    db: Session = Depends(get_db)
):

    record = StudentCourse(
        student_id=data.student_id,
        course_id=data.course_id
    )

    db.add(record)
    db.commit()

    return {
        "message": "Completed course added"
    }


@router.get("/")
def get_completed_courses(
    db: Session = Depends(get_db)
):
    return db.query(StudentCourse).all()
@router.put("/{record_id}")
def update_completed_course(
    record_id: int,
    data: StudentCourseCreate,
    db: Session = Depends(get_db)
):

    record = (
        db.query(StudentCourse)
        .filter(StudentCourse.id == record_id)
        .first()
    )

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Record not found"
        )

    record.student_id = data.student_id
    record.course_id = data.course_id

    db.commit()

    return {
        "message": "Academic history updated successfully"
    }
@router.delete("/{record_id}")
def delete_completed_course(
    record_id: int,
    db: Session = Depends(get_db)
):

    record = (
        db.query(StudentCourse)
        .filter(StudentCourse.id == record_id)
        .first()
    )

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Record not found"
        )

    db.delete(record)
    db.commit()

    return {
        "message": "Academic history deleted successfully"
    }