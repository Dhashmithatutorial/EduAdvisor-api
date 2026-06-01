from pydantic import BaseModel


class GPASimulationRequest(BaseModel):

    current_gpa: float

    current_credits: int

    new_course_credits: int

    expected_grade_points: float