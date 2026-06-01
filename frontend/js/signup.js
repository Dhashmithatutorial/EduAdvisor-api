async function signup(){

    const full_name =
        document.getElementById(
            "full_name"
        ).value;

    const email =
        document.getElementById(
            "email"
        ).value;

    const password =
        document.getElementById(
            "password"
        ).value;

    const response =
        await fetch(
            `${API_URL}/auth/register`,
            {
                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({
                    full_name,
                    email,
                    password
                })
            }
        );

    const data =
        await response.json();

    if(response.ok){

        document.getElementById(
            "message"
        ).innerText =
            "Account created successfully";

        setTimeout(() => {

            window.location.href =
                "login.html";

        },1500);

    }else{

        document.getElementById(
            "message"
        ).innerText =
            data.detail;
    }
}