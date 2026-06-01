from sqlalchemy import Column, Integer, String

from backend.database.connection import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    course_name = Column(String, nullable=False)

    credits = Column(Integer, nullable=False)

    category = Column(String, nullable=False)

    prerequisite = Column(String, nullable=True)