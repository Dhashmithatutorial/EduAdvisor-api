from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.models.course import Course
from backend.schemas.course_schema import CourseCreate

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    new_course = Course(
        course_name=course.course_name,
        credits=course.credits,
        category=course.category,
        prerequisite=course.prerequisite
    )

    db.add(new_course)
    db.commit()

    return {
        "message": "Course created successfully"
    }


@router.get("/")
def get_courses(
    db: Session = Depends(get_db)
):
    return db.query(Course).all()

@router.put("/{course_id}")
def update_course(
    course_id: int,
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    db_course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not db_course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db_course.course_name = course.course_name
    db_course.credits = course.credits
    db_course.category = course.category
    db_course.prerequisite = course.prerequisite

    db.commit()

    return {
        "message": "Course updated successfully"
    }


@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    db_course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not db_course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db.delete(db_course)
    db.commit()

    return {
        "message": "Course deleted successfully"
    }