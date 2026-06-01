from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from backend.database.db_init import create_tables
from backend.app.dependencies import get_db
from backend.models.user import User

from backend.routers.auth_routes import (
    router as auth_router
)
from backend.routers.course_routes import (
    router as course_router
)
from backend.routers.student_routes import (
    router as student_router
)
from backend.routers.student_course_routes import (
    router as student_course_router
)
from backend.routers.recommendation_routes import (
    router as recommendation_router
)
from backend.routers.gpa_routes import (
    router as gpa_router
)
from backend.routers.roadmap_routes import (
    router as roadmap_router
)

app = FastAPI(
    title="EduAdvisor API",
    version="1.0.0",
    description="API academic course recommendation platform"
)

create_tables()

app.include_router(auth_router)
app.include_router(course_router)
app.include_router(student_router)
app.include_router(student_course_router)
app.include_router(recommendation_router)
app.include_router(gpa_router)
app.include_router(roadmap_router)


@app.get("/")
def home():
    return {
        "message": "Academic Advisor API Running Successfully"
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)