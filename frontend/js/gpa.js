async function simulateGPA(){

    const current_gpa =
        parseFloat(
            document.getElementById(
                "current_gpa"
            ).value
        );

    const current_credits =
        parseInt(
            document.getElementById(
                "current_credits"
            ).value
        );

    const new_course_credits =
        parseInt(
            document.getElementById(
                "new_course_credits"
            ).value
        );

    const expected_grade_points =
        parseFloat(
            document.getElementById(
                "expected_grade_points"
            ).value
        );

    const response =
        await fetch(
            `${API_URL}/gpa/simulate`,
            {
                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({

                    current_gpa,

                    current_credits,

                    new_course_credits,

                    expected_grade_points

                })
            }
        );

    const data =
        await response.json();

    document.getElementById(
        "resultCard"
    ).style.display =
        "block";

    document.getElementById(
        "result"
    ).innerHTML =

        ` ${data.predicted_gpa}`;
}