// ================= ADD BOOK =================
function addBook() {

    let title = document.getElementById("title").value;
    let author = document.getElementById("author_name").value;

    if (title == "" || author == "") {
        alert("Please enter title and author");
        return;
    }

    fetch("http://127.0.0.1:8000/add_book/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            author_name: author
        })
    })
        .then(res => res.json())
        .then(data => {
            alert(data.Msg);
            location.reload();
        });
}


// ================= GET BOOKS =================
function getBooks() {

    fetch("http://127.0.0.1:8000/get_book/")
        .then(res => res.json())
        .then(data => {
            console.log("All Books:", data.data);
        });
}


// ================= LOAD EDIT =================
function loadEdit(id, title, author) {

    document.getElementById("editBox").style.display = "block";

    document.getElementById("uid").value = id;
    document.getElementById("utitle").value = title;
    document.getElementById("uauthor").value = author;

    window.scrollTo(0, 0);
}


// ================= UPDATE BOOK =================
function updateBook() {

    let id = document.getElementById("uid").value;
    let title = document.getElementById("utitle").value;
    let author = document.getElementById("uauthor").value;

    fetch(`http://127.0.0.1:8000/update_book/${id}/`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            author_name: author
        })
    })
        .then(res => res.json())
        .then(data => {
            alert(data.msg);
            location.reload();
        });
}


// ================= DELETE BOOK =================
function deleteBook(id) {

    if (!confirm("Are you sure to delete this book?")) {
        return;
    }

    fetch(`http://127.0.0.1:8000/delete_book/${id}/`, {
        method: "DELETE"
    })
        .then(res => res.json())
        .then(data => {
            alert(data.msg);
            location.reload();
        });
}

// ================= ISSUE BOOK =================
function issueBook(id, btn) {

    let row = btn.closest("tr");

    let borrower = row.querySelector(".borrower").value;
    let date = row.querySelector(".issuedate").value;

    if (borrower === "" || date === "") {
        alert("Please enter Student Name and Issue Date");
        return;
    }

    fetch(`http://127.0.0.1:8000/issue_book/${id}/`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            borrower: borrower,
            issue_date: date
        })
    })
        .then(res => res.json())
        .then(data => {
            alert(data.msg);
            location.reload();
        });
}


// ================= RETURN BOOK =================
function returnBook(id) {

    fetch(`http://127.0.0.1:8000/return_book/${id}/`, {
        method: "PUT"
    })
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                alert(data.msg + " | Fine: ₹" + data.fine);
                location.reload();
            }
        });
}



