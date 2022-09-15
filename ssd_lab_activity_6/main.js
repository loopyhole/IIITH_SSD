function emailCheck(){
    mailID = document.forms["myForm"]["grpEmail"];
    criteria = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (mailID.value.match(criteria)){
        document.getElementById("mailError").innerHTML = "";
    } else {
        document.getElementById("mailError").innerHTML = "Invalid Email";
    }
}

function unameCheck(){
    uname = document.forms["myForm"]["srvUsrname"];
    criteria = /(?=.\d)(?=.[a-z])(?=.[A-Z])./;
    if (uname.value.match(criteria)){
        document.getElementById("unameError").innerHTML = "";
    } else {
        document.getElementById("unameError").innerHTML = "Invalid username";
    }
}

function passCheck(){
    password = document.forms["myForm"]["pass"];
    otherPassword = document.forms["myForm"]["confPass"];
    if (password.value == otherPassword.value){
        document.getElementById("confError").innerHTML = "";
    } else {
        document.getElementById("confError").innerHTML = "Passwords don't match";
    }
}

function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData("text", event.target.innerHTML);
}

function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData("text");
    event.target.appendChild(document.getElementsByClassName("drag2"));
}
