/////////////setting the values to the old values
var currentobj  = localStorage.getItem("currentupdate");
console.log(currentobj);
//var currentobjp = JSON.parse(currentobj);
//console.log(currentobjp);
var obj = localStorage.getItem(currentobj);
console.log(obj);
var finalobj = JSON.parse(obj);

document.getElementById("new").value = finalobj["EmployeeName"];

document.getElementById("newID").value = finalobj["EmployeeID"];

document.getElementById("mail").value = finalobj["email"];

document.getElementById("num").value = finalobj["Phonenumber"];

document.getElementById("a").value = finalobj["Addres"];

document.getElementById("d").value = finalobj["Date"];

document.getElementById("s").value = finalobj["Salary"];

document.getElementById("vacdays").value = finalobj["a1"];

document.getElementById("approved").value = finalobj["a2"];

if(finalobj["gender"] === "female"){
    let defaultbtn = document.getElementById("female");
    defaultbtn.checked = "true";
}
else if(finalobj["gender"] === "male"){
    let defaultbtn = document.getElementById("male");
    defaultbtn.checked = "true";
}

if(finalobj["statue"] === "active"){
    let defaultbtn = document.getElementById("active");
    defaultbtn.checked = "true";
}
else if(finalobj["statue"] === "inactive"){
    let defaultbtn = document.getElementById("inactive");
    defaultbtn.checked = "true";
}

if(finalobj["MaritalStatue"] == "Single"){
    let defaultbtn = document.getElementById("single");
    defaultbtn.checked = "true";
}
else if(finalobj["MaritalStatue"] == "married"){
    let defaultbtn = document.getElementById("married");
    defaultbtn.checked = "true";
}

//console.log(document.getElementById("MS").value);
/*
document. querySelector('input[type = radio],input[name = gender]:checked'). value = finalobj["gender"];
//document.getElementById("gender").value = finalobj["Gender"];
console.log(document. querySelector('input[type = radio],input[name = gender]:checked'). value);
document.getElementById("statue").value = finalobj["statue"];
document.getElementById("Marital Status").value = finalobj["MARITALSTATUE"];
console.log(document.getElementById("statue").value);
*/
console.log()
document.forms[0].onsubmit = function(e){
    var EmployeeName=document.getElementById("new").value;
    var EmployeeID=document.getElementById("newID").value;
    var email=document.getElementById("mail").value;
    var Phonenumber=document.getElementById("num").value;
    var Addres=document.getElementById("a").value;
    var Salary=document.getElementById("s").value;
    var NumberVacation=document.getElementById("vacdays").value;
    var NumberApprovedVacation=document.getElementById("approved").value;
    var Date=document.getElementById("d").value;
    var gender = document.querySelector("input[name=gender]:checked").value;
    var statue = document.querySelector("input[name=status]:checked").value;
    var MaritalStatue = document.querySelector("input[name=mstatus]:checked").value;

    var user = {
        EmployeeName: EmployeeName,
        EmployeeID: EmployeeID,
        email: email,
        Phonenumber: Phonenumber,
        Addres: Addres,
        Salary: Salary,
        a1: NumberVacation,
        a2: NumberApprovedVacation,
        Date: Date,
        gender: gender,
        statue: statue,
        MaritalStatue: MaritalStatue,
    };

    var json = JSON.stringify(user);
    
    localStorage.setItem(EmployeeName, json);
    
}
localStorage.removeItem("currentupdate");
