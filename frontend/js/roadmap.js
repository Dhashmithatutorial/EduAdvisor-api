async function loadRoadmap(){

    const response =
        await fetch(
            `${API_URL}/roadmap/1`
        );

    const data =
        await response.json();

    const goals = {

        semester_1:
        "Build Programming Foundations",

        semester_2:
        "Learn Databases and AI Basics",

        semester_3:
        "Master Machine Learning",

        semester_4:
        "Become Industry Ready"

    };

    let html = "";

    Object.entries(data).forEach(

        ([semester,courses]) => {

            html += `

            <div class="card">

                <div class="badge">

                    ${semester
                    .replace("_"," ")
                    .toUpperCase()}

                </div>

                <h2>
                    ${goals[semester]}
                </h2>

                <br>

                <ul>

                    ${courses.map(

                        course =>

                        `<li>${course}</li>`

                    ).join("")}

                </ul>

            </div>

            `;

        }

    );

    document.getElementById(
        "roadmap"
    ).innerHTML = html;
}

loadRoadmap();