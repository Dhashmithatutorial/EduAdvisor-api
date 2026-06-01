async function loadStudent() {

    const response =
        await fetch(
            `${API_URL}/students`
        );

    const students =
        await response.json();

    const student =
        students[0];

    document.getElementById(
        "studentCard"
    ).innerHTML = `

        <h2>
             Welcome Back
        </h2>

        <p style="
        color:gray;
        margin-bottom:20px;
        ">
            Your personalized AI academic advisor is ready.
        </p>

        <div style="
        display:grid;
        grid-template-columns:
        repeat(auto-fit,minmax(220px,1fr));
        gap:20px;
        ">

            <div>

                <h3>
                    🎓 Student Profile
                </h3>

                <p>
                    <strong>ID:</strong>
                    ${student.user_id}
                </p>

                <p>
                    <strong>Department:</strong>
                    ${student.department}
                </p>

                <p>
                    <strong>Current GPA:</strong>
                    ${student.current_gpa}
                </p>

            </div>

            <div>

                <h3>
                     Career Information
                </h3>

                <p>
                    <strong>Interests:</strong>
                    ${student.interests}
                </p>

                <p>
                    <strong>Career Goal:</strong>
                    ${student.career_goal}
                </p>

            </div>

        </div>

    `;
}

async function loadRecommendations() {

    const response =
        await fetch(
            `${API_URL}/recommendations/2`
        );

    const courses =
        await response.json();

    document.getElementById(
        "stats"
    ).innerHTML = `

        <div class="card">

            <h3>
                Courses
            </h3>

            <h1>
                ${courses.length}
            </h1>

        </div>

        <div class="card">

            <h3>
                 GPA
            </h3>

            <h1>
                8.4
            </h1>

        </div>

        <div class="card">

            <h3>
                 Roadmap
            </h3>

            <h1>
                4
            </h1>

        </div>

        <div class="card">

            <h3>
                Career Goal
            </h3>

            <h1>
                AI
            </h1>

        </div>

    `;

    document.getElementById(
        "analytics"
    ).innerHTML = `

        <h2>
            Dashboard Analytics
        </h2>

        <p>
             Recommendation Engine:
            Active
        </p>

        <p>
             Recommended Courses:
            ${courses.length}
        </p>

        <p>
            GPA Simulator:
            Available
        </p>

        <p>
             Roadmap Generator:
            Active
        </p>

        <p>
            Secure JWT Authentication:
            Enabled
        </p>

    `;

    let html = "";

    courses.forEach(course => {

        html += `

            <div class="card">

                <div class="badge">
                    Recommended
                </div>

                <h2>
                    ${course.course_name}
                </h2>

                <p>
                    <strong>Category:</strong>
                    ${course.category}
                </p>

                <p>
                    <strong>Credits:</strong>
                    ${course.credits}
                </p>

                <p>
                    <strong>Prerequisite:</strong>
                    ${course.prerequisite ?? "None"}
                </p>

                <p>
                    <strong>Reason:</strong>
                    ${course.reason}
                </p>

                <br>

                <p style="
                color:#16a34a;
                font-weight:bold;
                font-size:18px;
                ">
                    ⭐ Score:
                    ${course.score}
                </p>

            </div>

        `;
    });

    document.getElementById(
        "recommendations"
    ).innerHTML = html;
}
function logout() {

    localStorage.removeItem(
        "token"
    );

    window.location.href =
        "login.html";
}

loadStudent();
loadRecommendations();