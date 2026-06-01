from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.app.dependencies import get_db

from backend.services.recommendation_service import (
    get_recommendations
)

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("/{student_id}")
def recommend_courses(
    student_id: int,
    db: Session = Depends(get_db)
):

    recommendations = get_recommendations(
        student_id,
        db
    )

    result = []

    for item in recommendations:

        course = item["course"]

        result.append(
            {
                "course_name":
                course.course_name,

                "category":
                course.category,

                "credits":
                course.credits,

                "prerequisite":
                course.prerequisite,

                "reason":
                f"Recommended based on {course.category} interest and aligns with career goals",  

                "score":
                item["score"]
            }
        )

    return result