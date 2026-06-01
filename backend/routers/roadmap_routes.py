from fastapi import APIRouter

router = APIRouter(
    prefix="/roadmap",
    tags=["Roadmap"]
)


@router.get("/{student_id}")
def get_roadmap(student_id: int):

    return {

        "semester_1": [
            "Python Programming",
            "Data Structures"
        ],

        "semester_2": [
            "DBMS",
            "Machine Learning"
        ],

        "semester_3": [
            "Deep Learning",
            "Big Data Analytics"
        ],

        "semester_4": [
            "Cloud Computing",
            "DevOps"
        ]

    }