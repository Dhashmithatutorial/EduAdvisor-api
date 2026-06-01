let editingStudentId = null;
async function saveStudent(){

    const student = {

        user_id: parseInt(
            document.getElementById("user_id").value
        ),

        department:
        document.getElementById("department").value,

        current_gpa: parseFloat(
            document.getElementById("gpa").value
        ),

        interests:
        document.getElementById("interests").value,

        career_goal:
        document.getElementById("career_goal").value
    };

    let url =
        `${API_URL}/students/`;

    let method =
        "POST";

    if(editingStudentId){

        url =
        `${API_URL}/students/${editingStudentId}`;

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

            body:JSON.stringify(student)
        });

    const data =
        await response.json();

    alert(data.message);

    editingStudentId = null;

    document.getElementById(
        "user_id"
    ).value = "";

    document.getElementById(
        "department"
    ).value = "";

    document.getElementById(
        "gpa"
    ).value = "";

    document.getElementById(
        "interests"
    ).value = "";

    document.getElementById(
        "career_goal"
    ).value = "";

    loadStudents();
}
async function loadStudents(){

    const response =
        await fetch(
            `${API_URL}/students/`
        );

    const students =
        await response.json();

        document.getElementById(
    "studentCount"
).innerText = students.length;

    let html = "";

    students.forEach(student => {

        html += `

        <tr>

            <td>${student.id}</td>

            <td>${student.user_id}</td>

            <td>${student.department}</td>

            <td>${student.current_gpa}</td>

            <td>${student.interests}</td>

            <td>${student.career_goal}</td>

            <td>

                <button
onclick="
editStudent(
${student.id},
${student.user_id},
'${student.department}',
${student.current_gpa},
'${student.interests}',
'${student.career_goal}'
)
"
style="
margin-right:10px;
background:#f59e0b;
"
>
Edit
</button>

<button
onclick="
deleteStudent(
${student.id}
)
"
style="
background:#ef4444;
"
>
Delete
</button>

            </td>

        </tr>

        `;
    });

    document.getElementById(
        "studentTable"
    ).innerHTML = html;
}


async function deleteStudent(
    id
){

    if(
        !confirm(
            "Delete Student?"
        )
    ){
        return;
    }

    await fetch(
        `${API_URL}/students/${id}`,
        {
            method:"DELETE"
        }
    );

    loadStudents();
}
function editStudent(
    id,
    user_id,
    department,
    gpa,
    interests,
    career_goal
){

    editingStudentId = id;

    document.getElementById(
        "user_id"
    ).value = user_id;

    document.getElementById(
        "department"
    ).value = department;

    document.getElementById(
        "gpa"
    ).value = gpa;

    document.getElementById(
        "interests"
    ).value = interests;

    document.getElementById(
        "career_goal"
    ).value = career_goal;

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });
}

loadStudents();