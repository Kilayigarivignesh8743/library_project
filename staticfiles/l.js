let login_btn = document.getElementById("login_btn")
login_btn.addEventListener("click", () => {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let role = document.getElementById("role").value;


    let login_p_d = {
        e: email,
        p: password,
        r: role

    }

    fetch("http://127.0.0.1:8000/login_validation/",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(login_p_d)
    }).then(res=>res.json())
    .then(data=>{
        console.log(data,"teach")
    window.location.href=`/${data.r_url}/${data.id}/`
    })
})

