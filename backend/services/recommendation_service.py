from backend.models.student import Student
from backend.models.course import Course
from backend.models.student_course import StudentCourse


def get_recommendations(student_id, db):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:
        return []

    interests = [
        interest.strip()
        for interest in student.interests.split(",")
    ]

    completed_course_ids = [
        record.course_id
        for record in db.query(StudentCourse)
        .filter(
            StudentCourse.student_id == student_id
        )
        .all()
    ]

    all_courses = db.query(Course).all()

    recommendations = []

    for course in all_courses:

        score = 0

        # Interest-based scoring
        if course.category in interests:
            score += 10

        # Career goal-based scoring
        if (
            "Machine Learning"
            in student.career_goal
            and course.category == "AI"
        ):
            score += 5

        # Prerequisite checking
        if course.prerequisite:

            prerequisite_course = (
                db.query(Course)
                .filter(
                    Course.course_name
                    == course.prerequisite
                )
                .first()
            )

            if (
                prerequisite_course
                and prerequisite_course.id
                not in completed_course_ids
            ):
                continue

        # Skip already completed courses
        if course.id in completed_course_ids:
            continue

        if score > 0:
            recommendations.append(
                {
                    "course": course,
                    "score": score
                }
            )

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations