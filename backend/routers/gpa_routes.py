from fastapi import APIRouter

from backend.schemas.gpa_schema import (
    GPASimulationRequest
)

router = APIRouter(
    prefix="/gpa",
    tags=["GPA Simulation"]
)


@router.post("/simulate")
def simulate_gpa(
    data: GPASimulationRequest
):

    total_points = (
        data.current_gpa
        * data.current_credits
    )

    total_points += (
        data.expected_grade_points
        * data.new_course_credits
    )

    total_credits = (
        data.current_credits
        + data.new_course_credits
    )

    predicted_gpa = (
        total_points
        / total_credits
    )

    return {
        "current_gpa":
        data.current_gpa,

        "predicted_gpa":
        round(predicted_gpa, 2)
    }