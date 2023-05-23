

let btn = document.getElementById("sbmtbtn");
var currentName = localStorage.getItem("currentName");

var obj = localStorage.getItem(currentName);
console.log(obj);
var finalobj = JSON.parse(obj);
console.log(finalobj);
document.getElementById("VEmpName").value = finalobj["EmployeeName"];
document.getElementById("empID").value = finalobj["EmployeeID"];

// if i am coming from vacation requests.
if(finalobj.hasOwnProperty('fromDate')){
    document.getElementById("fromDate").value = finalobj["fromDate"];
    document.getElementById("toDate").value = finalobj["toDate"];
    document.getElementById("VReason").value = finalobj["reason"];
    document.getElementById("Vstatus").value = finalobj["status"];

}

function onSubmit(e){
    let empNeme = document.getElementById("VEmpName").value;
    let empID = document.getElementById("empID").value;
    let fromDate = document.getElementById("fromDate").value;
    let toDate = document.getElementById("toDate").value;
    let reason = document.getElementById("VReason").value;
    let stat = document.getElementById("Vstatus").value;
    let date = new Date(toDate);
    let date2 = new Date(fromDate);
    if(date.getDate()-date2.getDate() <0)
    {
        document.getElementById("error").innerText = "Please check the dates";
        e.preventDefault();
        
    }
    else if(date.getDate()-date2.getDate()> finalobj.a1)
    {
        document.getElementById("error").innerText = `You have maximum ${finalobj.a1} days available` ;
        e.preventDefault();
    }
    finalobj.fromDate = fromDate;
    finalobj.toDate = toDate;
    finalobj.reason = reason;
    finalobj.status = stat;
    var json = JSON.stringify(finalobj);
    localStorage.removeItem(currentName);
    localStorage.setItem(empNeme, json);
    console.log("Vacation form has been submitted");
}

btn.onclick = onSubmit;
