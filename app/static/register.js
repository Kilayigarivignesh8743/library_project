let reg_btn = document.getElementById("reg_btn")
console.log("Register JS loaded");  

reg_btn.addEventListener("click", () => {
    console.log("Register button clicked");
    // e.preventDefault()
    let reg_data = {n : document.getElementById("name").value,
     e : document.getElementById("email").value,
     i : document.getElementById("id").value,
     d : document.getElementById("dept").value,
     ph : document.getElementById("ph_num").value,
     p: document.getElementById("password").value,
     cp: document.getElementById("c_password").value,
     r : document.getElementById("role").value
    };
    // let library_user = {
    //     n: name,
    //     e: email,
    //     i: id,
    //     d: dept,
    //     ph: ph_num,
    //     p: password,
    //     cp: c_password,
    //     r:role
    // };
    fetch("https://library-project-1-vhbe.onrender.com/register/",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(reg_data)
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data);

       alert(data.msg);

        window.location.href="/login/"
    })
    .catch(err=>{
        console.log(err)
        alert("Registrartion failed")
    })
    // .then(data=>console.log(data))
    // console.log(library_user)
})


