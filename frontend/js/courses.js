let editingCourseId = null;

async function saveCourse(){

    const course = {

        course_name:
        document.getElementById(
            "course_name"
        ).value,

        credits:
        parseInt(
            document.getElementById(
                "credits"
            ).value
        ),

        category:
        document.getElementById(
            "category"
        ).value,

        prerequisite:
        document.getElementById(
            "prerequisite"
        ).value
    };

    let url =
        `${API_URL}/courses/`;

    let method =
        "POST";

    if(editingCourseId){

        url =
        `${API_URL}/courses/${editingCourseId}`;

        method =
        "PUT";
    }

    const response =
        await fetch(url,{
            method:method,

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify(
                course
            )
        });

    const data =
        await response.json();

    alert(data.message);

    editingCourseId = null;

    document.getElementById(
        "course_name"
    ).value = "";

    document.getElementById(
        "credits"
    ).value = "";

    document.getElementById(
        "category"
    ).value = "";

    document.getElementById(
        "prerequisite"
    ).value = "";

    loadCourses();
}

async function loadCourses(){

    const response =
        await fetch(
            `${API_URL}/courses/`
        );

    const courses =
        await response.json();
        document.getElementById(
    "courseCount"
).innerText = courses.length;

    let html = "";

    courses.forEach(course => {

        html += `

        <tr>

            <td>${course.id}</td>

            <td>${course.course_name}</td>

            <td>${course.credits}</td>

            <td>${course.category}</td>

            <td>${course.prerequisite}</td>

            <td>

                <button
                onclick="
                editCourse(
                ${course.id},
                '${course.course_name}',
                ${course.credits},
                '${course.category}',
                '${course.prerequisite}'
                )
                "
                style="
                background:orange;
                margin-right:10px;
                "
                >
                    Edit
                </button>

                <button
                onclick="
                deleteCourse(
                ${course.id}
                )
                "
                style="
                background:red;
                "
                >
                    Delete
                </button>

            </td>

        </tr>

        `;
    });

    document.getElementById(
        "courseTable"
    ).innerHTML = html;
}

function editCourse(
    id,
    name,
    credits,
    category,
    prerequisite
){

    editingCourseId = id;

    document.getElementById(
        "course_name"
    ).value = name;

    document.getElementById(
        "credits"
    ).value = credits;

    document.getElementById(
        "category"
    ).value = category;

    document.getElementById(
        "prerequisite"
    ).value = prerequisite;

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });
}

async function deleteCourse(id){

    if(
        !confirm(
            "Delete Course?"
        )
    ){
        return;
    }

    await fetch(
        `${API_URL}/courses/${id}`,
        {
            method:"DELETE"
        }
    );

    loadCourses();
}

loadCourses();