# EduAdvisor API

## Academic Guidance and Course Recommendation Platform

### Project Overview

EduAdvisor API is a Full Stack Academic Guidance Platform developed using FastAPI, SQLite, HTML, CSS, and JavaScript.

The system helps students manage academic profiles, explore career opportunities, receive course recommendations, follow personalized learning roadmaps, and simulate GPA outcomes through an interactive web application.

---

## Key Features

### Authentication Module

* User Registration
* User Login
* JWT-Based Authentication

### Student Management

* Add Student Records
* View Student Profiles
* Update Student Information
* Delete Student Records

### Course Management

* Add Courses
* View Available Courses
* Edit Course Details
* Delete Courses

### Academic Guidance

* Career Insights Dashboard
* Personalized Learning Roadmap
* GPA Impact Simulator
* Course Recommendation Engine

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* JWT Authentication

### Frontend

* HTML5
* CSS3
* JavaScript

### Development Tools

* Visual Studio Code
* Swagger UI
* GitHub

---

## Project Structure

EduAdvisor-API/

backend/

* auth/
* database/
* models/
* routers/
* schemas/

frontend/

* css/
* js/
* login.html
* signup.html
* dashboard.html
* students.html
* courses.html
* career.html
* roadmap.html
* gpa.html

---

## API Endpoints

### Authentication

* POST /auth/register
* POST /auth/login

### Students

* GET /students
* POST /students
* PUT /students/{id}
* DELETE /students/{id}

### Courses

* GET /courses
* POST /courses
* PUT /courses/{id}
* DELETE /courses/{id}

### Recommendations

* GET /recommendations/{student_id}

### Roadmap

* GET /roadmap/{student_id}

### GPA Simulator

* POST /gpa/predict

---

## How to Run

### Create Virtual Environment

python -m venv .venv

### Activate Environment

Windows:

.venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Application

uvicorn backend.main:app --reload

### Open Swagger Documentation

https://eduadvisor-api.onrender.com/docs

### Run Frontend

Open frontend pages using Live Server in Visual Studio Code.

---

## Future Enhancements

* Cloud Database Integration
* Advanced Student Analytics
* Enhanced Recommendation Algorithms
* Mobile Responsive Design
* Role-Based Access Control

---

# Application Screenshots

## Home Page

![Home Page](screenshots/Index_Page.png.png)

## Login Page

![Login Page](screenshots/Login_Page.png.png)

## Signup Page

![Signup Page](screenshots/Signup_Page.png.png)

## Dashboard

![Dashboard](screenshots/Dashboard1.png.png)

## Dashboard Recommendations

![Dashboard Recommendations](screenshots/Dashboard2.png.png)

## Student Management

![Student Management](screenshots/Student_Management.png.png)

## Course Management

![Course Management](screenshots/Course_Management.png.png)

## Career Insights

![Career Insights](screenshots/Career_Insights.png.png)

## Learning Roadmap

![Roadmap](screenshots/Roadmap.png.png)

## GPA Simulator

![GPA Simulator](screenshots/GPA_Simulator.png.png)

# API Testing Using Thunder Client

## GET Student API

![GET Student](screenshots/GET_Student_API.png.png)

## POST Student API

![POST Student](screenshots/POST_Student_API.png.png)

## PUT Student API

![PUT Student](screenshots/PUT_Student_API.png.png)

## DELETE Student API

![DELETE Student](screenshots/DELETE_Student_API.png.png)

## GET Course API

![GET Course](screenshots/GET_Course_API.png.png)

## POST Course API

![POST Course](screenshots/POST_Course_API.png.png)

## PUT Course API

![PUT Course](screenshots/PUT_Course_API.png.png)

## DELETE Course API

![DELETE Course](screenshots/DELETE_Course_API.png.png)


## Team Members

| Name                    | Roll Number |
| ----------------------- | ----------- |
| Kundeti Naga Dhashmitha | 241FA04338  |
| Adusumalli Bhargavi     | 241FA04340  |
| Vadde Bhuvana Teja      | 241FA04341  |

---

## Institution

Vignan University

Department of B.Tech

Academic Year: 2025-2026

---

## Project Guide

Faculty Advisor

K. Rajashekar

---

## License

This project is developed for academic and educational purposes.
